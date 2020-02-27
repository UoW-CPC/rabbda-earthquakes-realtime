# rabbda-earthquakes-realtime

## Introduction
This application comes alongs with a series of solutions that aim to demonstrate how Big Data can be used to create complex and real-life Big Data applications.

Specifically, with this application, we present how to acquire real-time data from Rest APIs and store them to Hadoop HDFS.

The data source for this demo is related to earthquakes, source: [USGS science for a changing world](https://earthquake.usgs.gov).

USGS provides a [Rest API](https://earthquake.usgs.gov/fdsnws/event/1/) which will be using to request earthquakes data.
Sample request in csv format: [earthquakes](https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=2020-02-18T00:00:00.000Z&endtime=2020-02-19T00:00:00.000)

The steps to store these data to HDFS are the following:
 1. Request the data from the Rest API.
 2. Pre-process the data to remove headers and format date and time of the earthquakes.
 3. Save the data temporary to the host machine.
 4. Upload the data to HDFS.
 
 ## Getting started
 These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
 
 ### Download the repository
 The initial step is to download the repository in your local machine. To do so, run the following command:
 ```
 git clone https://github.com/UoW-CPC/rabbda-earthquakes-realtime.git
 ```
 
 ### Running the application
 Having download the repository you can now run the application.
 First move to the working directory by executing the command:
 ```
 cd rabbda-earthquakes-realtime
 ``` 
 Now execute the command:
 ```
 ls
 ```
 There you can see a folder and three files:
 * _earthquakes_, folder which contains python scripts used to perform steps 1-3 mentioned in the introduction paragraph. 
 * _requirements.txt_, file used to install packages used by python scripts.
 * _flume-earthquakes-realtime.conf_, file used by Flume service to perform step 4 mentioned in the introduction paragraph.
 * _README.md_, project description file.
 
 #### Requirements installation
 
 At this phase __install the requirements__ by running the command:
 
 ```
 pip install -r requirements.txt
 ```
 
 #### Run the Python application
 
 Having install the requirements you can now __run the python application__. 
 
 Move to the earthquakes folder:
 ```
 cd earthquakes
 ```
 and execute the earthquakes script:
 ```
 Python earthquakes.py
 ```
 By default the script makes a requests every 10 minutes. As an alternative you can pass a parameter to change this value. Example:
  ```
 Python earthquakes.py 2
 ```
 Now we have a request every 2 minutes.
 
 To see the results open a new terminal and move to the repository directory. There, you can see a new directory, _data_. If you move into this folder, there is a file called _earthquakes.csv_.
 
 To see its content run the following command:
   ```
 cat earthquakes.csv
 ```
 Alternatively, you can monitor file changes with the command:
 ```
 tail -F earthquakes.csv
 ```
 
 At this point, we have temporary stored the data in the local machine.
 
 #### Run the Flume Agent
  
 Now, its time to upload those data to HDFS. To do so, we use the [Flume service](https://flume.apache.org/).
 Open a new terminal and move once again to the rabbda-earthquakes-realtime directory.
 
 There we have to edit the _flume-earthquakes-realtime.conf_ file.
 Specifically, you need to edit the  _eq.sources.r1.command_ and _eq.sinks.k1.hdfs.path_ to match your local environment.
 
 
 Example: 
 ```
 eq.sources.r1.command = tail -F /home/user/rabbda-earthquakes-realtime/data/earthquakes.csv
 eq.sinks.k1.hdfs.path = hdfs://NameNode.Domain.com:8020/user/UserName/flume/realtime
 ```
 Now is time to __start the Flume agent__ and upload the data to HDFS.
 ```
 flume-ng agent --name eq --conf-file flume-earthquakes-realtime.conf
 ```
 Having done this, Flume agent starts monitor the _earthquakes.csv_ file for changes and uploads the data to HDFS.
 
 #### Verify the data in HDFS
 Finally, __go to Ambari Files View__ in the path specified previously and see the data sinking to HDFS in real-time.
 
 ## Architecture
<img width="732" alt="architecture" src="https://user-images.githubusercontent.com/32298274/75445139-bebad500-595c-11ea-830f-9850fa0e7dd0.png">


## Results
 ### Python
 ### Flume
 ### Ambari
 
 
 