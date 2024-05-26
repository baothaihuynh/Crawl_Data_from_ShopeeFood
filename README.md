# **Crawl Data From ShopeeFood using Selenium**  
![Image](https://i.imgur.com/QK76lEe.png)  



## **🔍Project Overview**  

- This is a project to collect data from restaurants that are currently operating online on the [shopeefood.vn](http://shopeefood.vn/) website using the Selenium library on Python. ShopeeFood is a platform that partners with restaurants to sell food online.  

- The results obtained from the project are a dataset of 3647 restaurants with information such as food prices, opening hours, location, and number of reviews,… for use in building a Sentiment Analysis model.    


## **📌Business Goal**  

Optimizing the data collection process using the Selenium library to obtain two data tables with the necessary information for building machine learning models.  

- **Restaurant Table:**  
    - RestaurantID: The unique identifier for each restaurant.  

    - Restaurant Name: The name of the restaurant.  

    - Address: The physical address of the restaurant.  

    - Time: The restaurant's operating hours.  

    - Price: The price range of the restaurant's food.  

- **Review Table:**  
    - UserID: The unique identifier for each review.   

    - User: The name of the person who wrote the review.  

    - Review Time: The date and time that the review was written.  

    - Rating: The reviewer's rating of the restaurant.  

    - Comment: The reviewer's written feedback about the restaurant.  
    
    - RestaurantID: The ID of the restaurant that the review is about.  


## **🗂Work Scope**

- Collect restaurant data from online [Website](https://shopeefood.vn/ho-chi-minh/food/deals).  

- Complete all information as per the two tables in the objectives outlined.  


## **💡Domain Knowledge**  

#### **What is Selenium?**

- Selenium is one of the most widely used open source Web UI (User Interface) automation testing [suite.It](http://suite.it/) was originally developed by Jason Huggins in 2004 as an internal tool at Thought Works. Selenium supports automation across different browsers, platforms and programming languages.  

- Selenium can be easily deployed on platforms such as Windows, Linux, Solaris and Macintosh. Moreover, it supports OS (Operating System) for mobile applications like iOS, windows mobile and android.  

- Selenium supports a variety of programming languages through the use of drivers specific to each language.Languages supported by Selenium include C#, Java, Perl, PHP, Python and Ruby.Currently, Selenium Web driver is most popular with Java and C#. Selenium test scripts can be coded in any of the supported programming languages and can be run directly in most modern web browsers. Browsers supported by Selenium include Internet Explorer, Mozilla Firefox, Google Chrome and Safari.  
![Image](https://huynhthaibao.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F35e3b43e-ce00-46c4-a295-07a0dee3bd1a%2F3f012c0b-53a9-48ca-a3cd-fcc99e4d27a3%2F1_6vHYMhpUPJvnzjH2ZcwMWg.png?table=block&id=356f0b84-5ea2-4a42-8347-6fd205aa5943&spaceId=35e3b43e-ce00-46c4-a295-07a0dee3bd1a&width=2000&userId=&cache=v2)  
[Read more...](https://www.javatpoint.com/selenium-tutorial)  

#### **What is Web Scraping?**  

- Web scraping refers to the extraction of data from a website. This information is collected and then exported into a format that is more useful for the user. Be it a spreadsheet or an API.  
![Image](https://huynhthaibao.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F35e3b43e-ce00-46c4-a295-07a0dee3bd1a%2Fa9821986-57c9-4a4a-8f7d-85e4e34ade3e%2Ffebf9de6-8a5a-4055-b274-e685485496f5.jpeg?table=block&id=52ffbc9c-f773-42d2-be5f-3e0c9e955597&spaceId=35e3b43e-ce00-46c4-a295-07a0dee3bd1a&width=2000&userId=&cache=v2)


## **💻Technologies and Tools**  

- Use the Selenium data collection library on Python.  


## **🛠Work Reference**  

#### **I. Crawl Links of All Page In Shopee Food**  


#### **II. Crawl Infomations Necessary**  


#### **III. Result**
