<h1>Sportopedia<h1>

<h3>Introduction<h3>

<h4>Business Use Case<h4>
  
Analytics has become immensely popular within the last decade especially within the sports industry. Now that sports have become more competetive, sport industries are turning to raw data to look for answers and solutions to enhance team performances and attract fans & consumers more effectively. 

<h4>Solution<h4>
  
My solution is using multiple historical sport datasets to develop a data warehouse that will forcast game and players statistics so that sport analysts can more effectively query and analyze the data to make better strategic decisions.
  
<h3>Demo<h3>

![46bw1c](https://user-images.githubusercontent.com/48367736/85785290-26104800-b6f7-11ea-813e-0780d9768b76.gif)

<h2>Presentation Slides<h2>
  
![Slides](https://docs.google.com/presentation/d/1UtgYyS_OzYd2eKISQA0PEFr8ZizZxolrx4JCywblnHA/edit?usp=sharing)

<h2> ETL Pipeline <h2>

<p> All datasets are stored in the AWS S3 Bucket. From there, data was extracted from the bucket and transformed using the parallel computing library, dask. Processed data was transferred and stored into Postgres. To manage the entire workflow of this pipeline, Apache Airflow was utilise because while Luigi runs tasks in the cron jobs, Airflow has it own local scheduler which allows me to scale the tasks independently. Queries from Postgres were displayed on Tableau. 
 
<img width="2035" alt="Screen Shot 2020-06-25 at 3 27 15 PM" src="https://user-images.githubusercontent.com/48367736/85786870-ad11f000-b6f8-11ea-9ca4-dc09eee8c089.png">

 
<h2> Repository Structure <h2>
Airflow
Dask      Includes batch processing scripts (Extract from s3 -- transform with Dask -- transfer to postgres)
Postgres  Includes Schema table of all data sources togehter
Config    Hidden credientials
Frontend  


<h3>Dataset<h3>

<p> 15 gigabyte of the datasets consists of games, teams, and players' statistical for basketball, footballl, and soccer divided by leagues and gender. 
<p> Below is a glimpse of the NBA teams and player raw dataset which entails their teams and individual statistics by season.<p>
  # list data sources

* List Datasets

<h3> Cluster Setup <h3>
  
  * what was used?
  
<h3> References <h3>






