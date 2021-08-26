# Brief projet : Cas Pratique 
Réidentification faciale via une interface
Du 28/6/2021 au 2/7/2021 et du 26/7/2021 au 28/7/2021


## Context

You are new to an Artificial Intelligence service company.
Your first mission concerns the project of a chain of nightclubs that wants to build up and take advantage of a file of its customers (We will go over the legal implications here, but take the opportunity to find out!).
She wants to implement a system that can scan the faces of her customers to link them to a history (attendance, violence, over-consumption, ...).


### Goals
The company is only in an experimental phase, it asks you to produce a POC and your opinion on the subject. Currently having no platform, she wants an url on which she can upload a photo and observe the results.
The product must therefore include a simple interface making it possible to upload a photo as input to the neural network, and to display the result of the query on the database. For the content of this database, the client asks you about what you would find interesting in such a case (Person details? Incident prevention? Implementation of a blacklist system? Offers for regulars? Assimilation to a group of customers? ...).
### Characteristics
The client will provide you with an AI brick for face detection, which needs to be improved by supplementing it in particular with a facial re-identification part.
Also face detection should work for photos with a single individual or on a group of people.
### Major steps
From the specifications drawn up by the client, we will go to a demonstration website where the client can load an image containing one or more faces and the platform will be able to recognize the people in the image if they are in the database. of the company and display the information relating to each person.
The project has several levels and will be built over several iterations. The levels of implementation are:
The choice of artificial intelligence:
* AI must be capable of multi-face detection, robust in poor lighting conditions (especially night lighting), easily scalable (from image to video, for example) and fast.
* The interface:
* The interface must be simple, easy to use and above all robust to regression tests.
Legal:
* The legal aspect of the project must also be taken into account, as the client has the will to store sensitive personal data, in particular questions relating to image rights must be resolved unambiguously. The client will also want a blacklist system managed by an algorithm, the latter must be robust, moreover the decision-making system must be conditioned by human approval.
* Business intelligence:
The customer wishing to set up offers for regulars as well as a segmentation of his clientele, it is interesting to put a layer of processing of the data stored in the base on a regular basis to determine the habits of the customers, the frequency, the possible consumption. (although it is complicated to determine this information).
In this answer, I present the first version of the product in the form of POC, a simple interface that allows you to upload an image, detect faces and search for information about detected people.

## Installation

```python
pip install -r requirements.txt

```

## runinig
After activate python environment
```python
cd face_detection
python manage.py runserver

```

## Improvements and perspectives:
This first POC addresses the client's main problem, namely the possibility of using artificial intelligence to detect the faces of clients at the entrance to the nightclub, for example. This solution makes it possible to feed a database, to present a simple interface. The most important point is that it can easily evolve into video because the DeepFace library has bricks that allow it, in addition to the use of Django and the implementation of a simple model for the database will allow to make it more complex without difficulty.
However, this solution has limitations that must be addressed and that I have not yet integrated:
* Add the administration part which will allow access control.
* Add the people detected and who are not in the database.
* The calculation time of the proposed solution is too slow and needs to be reduced.
* The security of the platform is not yet thought through.
* Issues related to image rights must be considered and a sparse use of data storage is necessary.
* The business intelligence part can be implemented easily, however, customer consumption is complicated to determine and must be considered holistically in relation to other nightclub tools.
* Add the historical and incident tables.

## License
[MIT](https://choosealicense.com/licenses/mit/)
