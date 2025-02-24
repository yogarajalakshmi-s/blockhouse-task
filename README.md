## Project Overview
This project implements a simple backend service that exposes REST APIs for handling trade orders. The application is containerized using Docker and deployed on an AWS EC2 instance. A CI/CD pipeline is set up using GitHub Actions.    

### Features
1. REST API endpoints:
POST /orders: Accepts trade order details (symbol, price, quantity, order type)    
GET /orders: Returns the list of submitted orders
2. Data storage in PostgreSQL
3. Containerized application using Docker
4. Deployment on AWS EC2

### Technical Stack
1. Backend: [Python (FastAPI) or Golang (Gin/Echo)]
2. Database: PostgreSQL
3. Containerization: Docker
4. Cloud Platform: AWS EC2

### Current Status
The application has been developed and containerized successfully. However, there are ongoing issues with the EC2 deployment phase, specifically related to PostgreSQL connection.

### Known Issue
Unable to access the application on EC2 due to PostgreSQL connection problems. The error suggests that the application is trying to connect to PostgreSQL using "localhost", which doesn't work when the database is in a separate container.

### Setup and Deployment
1. Clone the repository
2. Build the Docker image:
`docker build -t blockhouse-app .`
3. Create a Docker network:
`docker network create blockhouse-network`
4. Run the PostgreSQL container:
`docker run --name postgres-container --network blockhouse-network -e POSTGRES_PASSWORD=your_secure_password -p 5432:5432 postgres`
5. Run the application container:
`docker run --network blockhouse-network --add-host=localhost:postgres-container -p 8000:8000 blockhouse-app`

<img width="1508" alt="Screenshot 2025-02-23 at 11 30 09 PM" src="https://github.com/user-attachments/assets/83921483-0c4d-49ba-8d60-b114f93abbe9" />
<img width="1508" alt="Screenshot 2025-02-23 at 11 41 12 PM" src="https://github.com/user-attachments/assets/9dadb2b9-bd0d-496c-b1d1-b86c5d3cbd85" />
