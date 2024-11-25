# **Reddit Data Pipeline 🚀**  

### **Overview**  
This project is a distributed data pipeline designed to fetch and process data from Reddit using **Apache Airflow**, **Celery**, and **Postgres**, while leveraging AWS services like **Glue**, **S3**, **Athena**, and **Redshift** for storage and analysis.

### **Pipeline at a Glance**  
![pipeline](https://github.com/user-attachments/assets/b426b8b2-9627-446c-91d5-4d6c241ff4ca)


- **Reddit** 🛠️: Source of the data.  
- **Airflow** 🔗: Orchestrates and schedules tasks.  
- **Celery** ⚙️: Distributes data-fetching tasks across workers.  
- **Postgres** 📊: Tracks task statuses and logs errors.  
- **Amazon S3** 🗃️: Stores raw and processed data.  
- **AWS Glue** 🧹: Catalogs and transforms data.  
- **Amazon Athena & Redshift** 📈: Enables querying and analysis of stored data.  

---

## **How It Works**  

### **1. Connecting to Reddit API 🔑**  
- Airflow uses a stored **API key** to connect to Reddit.  
- The subreddits to fetch data from are defined in the **DAG** (e.g., r/technology, r/science).  

### **2. Task Assignment 🗂️**  
- Airflow breaks the workflow into tasks (e.g., fetch data from r/technology).  
- These tasks are sent to **Celery**, which assigns them to workers for execution.  

### **3. Parallel Data Fetching 🏃‍♂️🏃‍♀️**  
- Celery workers fetch data from subreddits in parallel.  
  - Example:  
    - Worker 1: Fetches from r/technology.  
    - Worker 2: Fetches from r/science.  

### **4. Tracking and Storage 📋**  
- **Postgres** logs task statuses (success/failure) for monitoring and debugging.  
- Fetched data is stored in **Amazon S3** as raw files.  

### **5. Data Transformation and Querying 💡**  
- **AWS Glue** crawls and transforms data into a structured format.  
- Data is queried using **Athena** or analyzed in **Redshift** for advanced use cases.  

---

## **Why This Pipeline?**  
- **Scalable**: Parallel task execution using Celery.  
- **Modular**: Components like Airflow and Postgres are Dockerized for easy management.  
- **Cloud-Native**: Leverages AWS for storage and querying.  
- **Error-Resilient**: Logs tasks and errors for better debugging.  

---

## **Setup and Installation**  

### **Requirements**  
- Docker  
- Python 3.x  
- Apache Airflow  
- Celery  
- Postgres  
- AWS Account (for S3, Glue, Athena, and Redshift)  

### **Steps to Run**  
1. Clone this repository:  
   ```bash
   git clone https://github.com/delanie-06/Reddit_Pipeline_UsingAWS.git
   cd Reddit_Pipeline_UsingAWS
   ```  

2. Set up the Docker environment:  
   ```bash
   docker-compose up
   ```  

3. Configure your **Reddit API key** in the `.env` file:  
   ```env
   REDDIT_API_KEY=your-api-key
   ```  

4. Define subreddits in the DAG file:  
   ```python
   subreddits = ["technology", "science", "movies"]
   ```  

5. Access the Airflow UI:  
   - Go to `http://localhost:8080` and trigger the DAG to start data fetching.  

---

## **Folder Structure**  
```
reddit-data-pipeline/
├── dags/                  # Airflow DAGs
├── workers/               # Celery workers
├── postgres/              # Postgres setup
├── s3/                    # S3 integration
├── docker-compose.yml     # Docker orchestration
├── README.md              # Documentation
└── .env                   # Environment variables
```

---

## **Screenshots and Visuals**  

### **1. Pipeline Architecture**  
![pipeline](https://github.com/user-attachments/assets/f4e49c77-540a-49ad-a1de-5806c3cba6ca)
 

### **2. Airflow DAG Example**  
![dag](https://github.com/user-attachments/assets/d9adc42e-d5a5-4d32-a809-5f3e7371a28f)
  

### **3. S3 buckets**  
![s3](https://github.com/user-attachments/assets/d58d26f1-c740-4e9a-bf8f-ec791ea77df0)
  


### **4. Athena quering and insights**  
![athena](https://github.com/user-attachments/assets/3d63dcd9-d09a-40e5-a2e4-8d2bf94b5340)


---

### **Sentiment Analysis 📊**

After collecting Reddit data, I performed sentiment analysis to understand the emotions and opinions in the comments/posts. This step helps identify whether the content is positive, neutral, or negative.

#### **Tools Used**
- **Google Colab**: For running the sentiment analysis in a Jupyter Notebook environment.
- **TextBlob**: To calculate sentiment polarity (ranging from -1 for negative to +1 for positive).

 **Analyzing Polarity**:
   - Calculated the sentiment polarity for each comment using TextBlob.
   - Classified sentiments into three categories:
     - **Positive**: Polarity > 0
     - **Neutral**: Polarity = 0
     - **Negative**: Polarity < 0

**Visualization**:
   - **Distribution of Sentiment Polarity**: Showed how the sentiments are spread across the dataset.
   - **Sentiment Category Counts**: Highlighted the number of comments in each sentiment category.
   
![Screenshot 2024-11-26 020952](https://github.com/user-attachments/assets/31ab50f3-e065-4f70-aad3-787ecd6d986a)


![Screenshot 2024-11-26 021006](https://github.com/user-attachments/assets/de2982ab-fc24-4b51-b3fe-b761b84c6768)


#### **Key Observations**
- The majority of the sentiments were **neutral**, indicating most Reddit comments are factual or objective.
- A smaller portion of the comments leaned toward **positive** or **negative** sentiments.

---


## **Future Improvements**  
- Add analytics dashboards for real-time insights.  
- Include automated retries for failed tasks.  
- Integrate advanced processing like sentiment analysis.  

---

## **Contributors**  
- [DELANIE RODRIGUES](https://github.com/delanie-06)  
