# ☁️ Flask MySQL Products API with AWS Integration

### Created by: Vainavi Roy

Hi, I'm **Vainavi Roy**, a passionate computer science student with a strong interest in **cloud computing** and **backend development**. I built this project to deepen my understanding of AWS services and showcase my ability to design a **secure, scalable API** using industry best practices. This project serves as a great way to demonstrate **real-world AWS deployment skills** and create a foundation for more complex cloud applications.

## 🚀 Features
- Store product details via a **POST** request.
- Retrieve all stored products via a **GET** request.
- Uses **AWS RDS** as the database for scalable and managed SQL storage.
- Deployed on **AWS EC2** with a secure Virtual Private Cloud (VPC) setup.
- Follows best security practices by keeping the database in a **private subnet**.
- Implements **AWS Security Groups** to control access.
- Simple and lightweight, perfect for demonstrating cloud application development!

## 🏗️ Tech Stack
- **Python** 🐍 (Flask framework)
- **MySQL** 🗄️ (Database hosted on AWS RDS)
- **AWS EC2** 💻 (Compute instance for the API)
- **AWS RDS** ☁️ (Managed database service)
- **AWS VPC** 🔒 (Secure networking setup)
- **AWS Security Groups** 🚧 (Access control management)
- **Docker** 🐳 (Optional for local deployment)

---

## 🔧 AWS Setup and Deployment

### 1️⃣ Setting Up the AWS Environment
- **Created a VPC** to manage a secure private cloud network.
- **Configured Subnets**: 
  - Public subnet for **EC2** to allow external API access.
  - Private subnet for **RDS** to prevent direct public access.
- **Set Up Security Groups** to restrict database access to the EC2 instance only.

### 2️⃣ Launching an EC2 Instance
- Created an **Ubuntu 20.04 LTS EC2 instance**.
- Allowed inbound traffic for:
  - **Port 22** (SSH) - Secure remote access.
  - **Port 80/443** (HTTP/HTTPS) - API communication.
- Installed necessary dependencies:
  ```bash
  sudo apt update
  sudo apt install python3-pip
  pip3 install flask mysql-connector-python
  ```

### 3️⃣ Setting Up an RDS Database
- Created a **MySQL database instance on AWS RDS**.
- Configured it in a **private subnet** for security.
- Connected the Flask app to the database by adding RDS credentials in `app.py`:
  ```python
  db_config = {
      "host": "your-rds-endpoint.amazonaws.com",
      "user": "your-username",
      "password": "your-password",
      "database": "product_db"
  }
  ```

### 4️⃣ Deploying the Flask Application on EC2
- Cloned the repository onto the EC2 instance:
  ```bash
  git clone https://github.com/YOUR_GITHUB_USERNAME/flask-mysql-products.git
  cd flask-mysql-products
  ```
- Ran the Flask app:
  ```bash
  python3 app.py
  ```
- The API is now accessible via the **EC2 public IP**.

---

## 📌 API Endpoints

### 📝 Store Products
**POST** `/store-products`
- **Request Body (JSON):**
```json
{
  "products": [
    { "name": "Laptop", "price": "1200", "availability": true },
    { "name": "Mouse", "price": "25", "availability": false }
  ]
}
```
- **Response:**
```json
{ "message": "Success." }
```

### 📜 List Products
**GET** `/list-products`
- **Response:**
```json
{
  "products": [
    { "name": "Laptop", "price": "1200", "availability": true },
    { "name": "Mouse", "price": "25", "availability": false }
  ]
}
```

---

## ☁️ AWS Integration Details
✅ **EC2 for API Hosting:** The Flask application runs on an AWS EC2 instance with a public IP.  
✅ **RDS for Data Persistence:** The MySQL database is hosted on AWS RDS inside a **private subnet**.  
✅ **VPC Security:** The database is protected and only accessible from the EC2 instance.  
✅ **Security Groups:** Properly configured to allow only HTTP and SSH access to the EC2 instance.  
✅ **Auto Scaling Ready:** Can be expanded with Load Balancer & Auto Scaling groups.

---

## 🔥 Why I Built This Project
As someone passionate about **cloud computing and backend development**, I wanted to apply my AWS knowledge by building something practical. This project allows me to:
- Demonstrate **real-world AWS deployment skills**.
- Gain experience in **cloud security and architecture**.
- Show recruiters my ability to build **scalable and secure cloud applications**.

If you're looking for someone who understands **AWS, backend development, and secure API design**, I'd love to connect!

---

## 🏆 Contributing
Feel free to fork this repo and improve the API! Pull requests are welcome. 😊

---

## 📜 License
This project is **open-source** and available under the MIT License.

---

## 📬 Contact
For any questions, feel free to connect with me on **GitHub** or **LinkedIn**! 🎯

