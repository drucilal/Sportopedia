<h1>Sportopedia<h1>

<h3>Introduction<h3>

<h4>Business Use Case<h4>
  
Analytics has become immensely popular within the last decade especially within the sports industry. Now that sports have become more competetive, sport industries are turning to raw data to look for answers and solutions to enhance team performances and attract fans & consumers more effectively. 

<h4>Solution<h4>
  
My solution is using multiple historical sport datasets to develop a data warehouse that will forcast game and players statistics so that sport analysts can more effectively query and analyze the data to make better strategic decisions.
  
<h3>Demo<h3>
* Put video *

<h2>Presentation Slides<h2>

<h2> ETL Pipeline <h2>

<p> All datasets are stored in the AWS S3 Bucket. From there, data was extracted from the bucket and transformed using the parallel computing library, dask. Processed data was transferred and stored into Postgres. To manage the entire workflow of this pipeline, Apache Airflow was utilise because while Luigi runs tasks in the cron jobs, Airflow has it own local scheduler which allows me to scale the tasks independently. Queries from Postgres were displayed on Tableau. 
 
 ** screen shot of pipeline **
 
<h2> Repository Structure <h2>



<h3>Dataset<h3>

<p> 15 gigabyte of the datasets consists of games, teams, and players' statistical for basketball, footballl, and soccer divided by leagues and gender. 
<p> Below is a glimpse of the NBA teams and player raw dataset which entails their teams and individual statistics by season.<p>
  # list data sources

* List Datasets

<h3> Cluster Setup <h3>
  
  * what was used?
  
<h3> References <h3>






