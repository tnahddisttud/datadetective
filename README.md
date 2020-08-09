# datadetective-web

## Instructions for Environment setup in Windows

- Open Windows Powershell
- Clone Repo using `git clone https://github.com/HacKP-CyberDome/datadetective-web`
- Run `cd datadetective-web`
- `python3 -m venv .`
- `venv\Scripts\Activate.ps1`
- `pip3 install django==2.2.4`
- `cd backend/server`
- Run initiated server with the following command:
- `python manage.py runserver`

Now enter `127.0.0.1:8000` in your favorite web browser you should see default Django welcome site.




![Logo](https://github.com/HacKP-CyberDome/datadetective-web/blob/master/final_logo.png?raw=true)

> *“The world is full of obvious things which nobody by any chance ever observes.”***― Arthur Conan Doyle, “The Hound of the Baskervilles”**

Indian Police have long used brains and brawn,but now “**dataDetective**” a predictive policing tool using Big Data Analysis promises to make them more efficient.
The premise is simple: criminals follow patterns, and with our web based application,police can determine where the next crime will occur and can prevent it.
The key to success in predictive policing is getting as much data as possible to determine patterns.

With the advent of the Big Data era and the availability of fast, efficient algorithms for data analysis, understanding patterns in crime from data is an active and growing field of research. To be well prepared in responding to criminal activity, it is important to understand patterns in crime.



### Data

We have used Boston city’s crime data which is updated daily and is readily available [here](https://data.boston.gov/dataset/crime-incident-reports-august-2015-to-date-source-new-system/resource/12cb3883-56f5-47de-afa5-3b1cf61b257b). Crime incident reports are provided by Boston Police Department (BPD) to document the initial details surrounding an incident to which BPD officers respond. Our model will work fine with any other dataset of any other city if it contains the same features.



### Implementation

The term Artificial Intelligence (machine learning/deep learning) can be used to automatically detect meaningful patterns in data. It all starts with collecting the data. Dataset which we used was scraped from the website of Boston Police Dept. which is publically available. Using the Google Colab Jupyter environment we built our model using python and its libraries such as numpy and pandas packages,which are used for data manipulation.

### Data pre-processing

In the data set, there are NA values and Timestamp columns. In the current implementation it can not handle NA values and Timestamp columns, hence by applying pre-processing algorithms. All the NA values and the timestamp having a format of 2018-02-28 21:00:00 were dropped to split in separate columns like Day, Date, Year and Time.

### Algorithms training

After pre-processing, the next step was to select and extract the features of interest and then divide the data into training and testing using Pandas and Sci-Kit Learn libraries in python. For ML algorithm training the Random Forest, Decision Tree, KNN and Neural network algorithms from the Sci-Kit Learn Library were implemented. Out of which Random Forest Algorithm gave the most accurate and predictive output.

### Backend Development

Created a Django server with database models and REST API endpoints which represents ML endpoints, models and requests.. After getting the ML code ready and tested. It was connected with the server code. For this, we created the ML registry object, that keeps information about available algorithms and corresponding endpoints.

### Frontend Development

Diving into UI development, We designed and created a webapp to display the Heat Map, Search field and Results section. Once the UI was developed ,the front end was connected with the backend. Our application will send a request to the server and the server will send a response in JSON format which will be decoded and deserialized in the webapp and displayed results in the results section.

### Deployment

Our application is deployed on a docker container for our server code. With docker it is easy to deploy the code to selected infrastructure and it is easier to scale the service if needed. In this dockerfile, we load the ubuntu system, and install all needed packages and switch default python to python 3.6. Dockerfiles were defined for nginx server and our application.

### Vision

Going beyond homeland security can be instrumental in maintaining law and order by tracking and subverting terror activity by designing algorithms based on past activities and predicting the future.
While no technology can replace human intuition, similarly, predictive policing needs to be complemented by strong analytical skills of the police personnel. However, it is also pertinent that the government holds civil liberties and privacy at utmost importance. A robust mechanism to check violations and misuse along with sound judgement must be applied while implementing a predictive policing strategy.
The success of the model in the US and UK can be a learning point for adapting it to Indian needs and resources. AI powered predictive policing, coupled with higher resource allocation for law enforcement and evolved laws is the next-gen policing that our policing apparatus need to adapt to, to suit the emerging needs and times for outsmarting criminals with the power of data.

### Impact

- **Hotspot Analysis**
  One of the key features of the ambitious project is Hot Spot analysis wherein police personnel will analyze and predict geographical areas of increased crime on the basis of crime data. Hot sport analysis will process all patterns relating to time of occurrence, exact locations, even shops, hotels, bars or other establishments.
- **Crime pattern identification**
  dataDetective would help to identify the trends and determine the specific rhythm followed by a particular criminal activity to determine the possibility of that crime at a given location in future.
  Crime prediction
- **Redeployment of police resources**
- **Increase efficiency in policing and crime solving**
  The product we deliver would substantially increase efficiency in policing and crime solving, as the traditional policing realms would be updated with a faster and sophisticated technological interface, ensuring a reliable and productive outcome to identify the possibility of a crime. This combination would reflect in bringing a significant change in identifying the crimes, especially leading to woman and child abuse, saving a lot of police time for first level of inquiry.

### Future/Vision

While no technology can replace human intuition, similarly, predictive policing needs to be complemented by strong analytical skills of the police personnel. However, it is also pertinent that the government holds civil liberties and privacy at utmost importance. A robust mechanism to check violations and misuse along with sound judgement must be applied while implementing a predictive policing strategy.

### Screenshots

![Result Page](https://github.com/HacKP-CyberDome/datadetective-web/blob/master/result%20page.png?raw=true)

![Main Page](https://github.com/HacKP-CyberDome/datadetective-web/blob/master/main%20page.png?raw=true)


