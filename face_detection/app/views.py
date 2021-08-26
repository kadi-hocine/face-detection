from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
import json
from .models import Customer
from .forms import CustomerForm, CustomerFormImage
from django.core import serializers

from deepface import DeepFace
import cv2
from PIL import Image
import numpy as np
import glob
import pandas as pd
import os

#Page Home
def index(request):
    return render(request, 'home/index.html')


#Page liste des clients
def listCustomers(request):
    customers = Customer.objects.all()
    context={'customers': customers}
    return render(request, "home/listCustomers.html", context)

#Page ajouter un client
#L'utilisateur remplie le formulaire (nom, prénm,..) et ajoute une image
def addCustomer(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            img_obj = form.instance
            
            # On vérifie si le client ajouté n'existe pas dans la base.
            # On applique DeepFace.find pour détecter le visage puis le comprarer un à un aux visages stockés dans la base
            df = DeepFace.find(img_path = "../dataset"+img_obj.image.url, db_path = "../face_detection/images")

            #si le visage détecté n'est pas dans la base, on l'ajoute
            if (df["VGG-Face_cosine"] < 0.3).sum() == 0:
                #On standrdize la taille des images avant la sauvegarde
                target_size = (100, 100)
                form.save()
                detected_face,_,_  = DeepFace.detectFace("../face_detection/"+img_obj.image.url, detector_backend="retinaface")

                img_detected = cv2.resize(detected_face, target_size)
                cv2.imwrite("../face_detection/"+img_obj.image.url, img_detected)
                
                #on renvoie la page addCustomer
                return render(request, 'home/addCustomer.html', {'img_obj': img_obj, 'form': form})
            #si le visage détecté est déjà dans la bdd alors on renvoie la page indiquant que ce client existe déjà
            else:
                return render(request, 'home/existsCustomer.html', {'img_obj': img_obj, 'form': form})

    else:
        form = CustomerForm()
    return render(request, 'home/addCustomer.html', {'form': form})

#Page chercher les clients dans une image
path_temporaries_images = './images/temporary_images/'

#sur image présentant plusieurs visages, certains sont dans la bdd d'autres non
def searchCustomer(request):
    if request.method == 'POST':
        #le premier enverra les visages qui sont dans la bdd
        context = {}
        #le second ceux ui ne le sont pas 
        context2 = {}
        form2 = CustomerFormImage(request.POST, request.FILES)
        if form2.is_valid():
            img_obj = form2.instance
            img_path = "../dataset"+img_obj.image.url

            #L'image sera traitée par RetinaFace qui détectera tous les visage
            _, _, faces = DeepFace.detectFace(img_path = img_path, detector_backend="retinaface")

            
            # Supprimer le contenu du dossier temporaire
            files = glob.glob(path_temporaries_images+'*')
            for f in files:
                os.remove(f)

            #Enregistrer les visage détectés dans le dossier temporaire (une image par visage)
            index = 0
            for face in faces:
                index += 1
                cv2.imwrite(path_temporaries_images+str(index)+'.jpg', face[:,:,::-1])
            
            #Lister les images dans le dossier temporaire
            images_temps = glob.glob(path_temporaries_images+'/*')

            # Définir le seuil de détection
            threashold =  0.3
            images_in_BDD = []
            customers_out = []
            #On parcours les images (visages) :
            for imag in images_temps:
                #On vérifie si le visage existe dans la bdd
                df = DeepFace.find(imag, db_path = "../face_detection/images", enforce_detection=False)

                #s'il n'existe pas on l'ajoute à la liste customers_out
                if (df.empty) or ((df["VGG-Face_cosine"] < threashold).sum() == 0):
                    customers_out.append(imag)
                #sinon on l'ajoute à images_in_BDD
                else:
                    img_path_i = 'images'+df[df["VGG-Face_cosine"] < threashold]["identity"][0][24:]
                    images_in_BDD.append(img_path_i)
            #si aucun visage n'est détectés on revoie la page aucun clients n'a été trouvé 
            if images_in_BDD == []:
                context2 = {'customers_out': customers_out}
                return render(request, 'home/notexistsCustomer.html', context2)
            #sinon on renvois deux context le premier va remplir un tableau des visages qui sont dans la bdd
            #avec les infos de chacun, et le deuxième la liste des visages (images) qui ne sont pas dans la bdd
            else:
                customers_in = []
                for image_in_BDD in images_in_BDD:
                    #pour chaque visage qui est dans la bdd on récupère ces infos en utilisant le get sur l'url de l'image               
                    customer = Customer.objects.get(image=image_in_BDD)
                    customers_in.append(customer)
                context = {'customers_in': customers_in,
                           'customers_out': customers_out,}
                return render(request, 'home/searchCustomer.html', context)
    else:
        form2 = CustomerFormImage()
    return render(request, 'home/searchCustomer.html', {'form2': form2})

