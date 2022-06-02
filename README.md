# Black-Friday-Sales-Prediction

<p>Successfully established a machine learning model which can accurately predict the net Black Friday sales for a specific customer, based on various characteristics pertaining to that particular customer.</p>

![Black Friday Sales Prediction](https://i.ytimg.com/vi/ID8Lz5vR3qE/mqdefault.jpg)
![Black Friday Sales Prediction](https://camo.githubusercontent.com/1fada135d320c87bb1a851c584f697266a00f4279d2f5e977790c4d75d5aa780/68747470733a2f2f736561726368656e67696e656c616e642e636f6d2f6669677a2f77702d636f6e74656e742f73656c6f6164732f323031342f31322f626c61636b2d667269646179312d73732d313932302e6a7067)
![Black Friday Sales Prediction](https://businessyield.com/wp-content/uploads/2020/10/images-17.jpeg)

## Deployed Web Application

Link: https://black-friday-sales-forecast.herokuapp.com/

## About Dataset

<p>A retail company “ABC Private Limited” wants to understand the customer purchase behaviour (specifically, purchase amount) against various products of different categories. They have shared purchase summary of various customers for selected high volume products from last month.
The data set also contains customer demographics (age, gender, marital status, citytype, stayincurrentcity), product details (productid and product category) and Total purchaseamount from last month.</p>

<p>Now, they want to build a model to predict the purchase amount of customer against various products which will help them to create personalized offer for customers against different products.</p>

## Data

<table>
  <tr>
    <th>Variable</th>
    <th>Definition</th>
  </tr>
  <tr>
    <td>User_ID</td>
    <td>User ID</td>
  </tr>
  <tr>
    <td>Product_ID</td>
    <td>Product ID</td>
  </tr>
  <tr>
    <td>Gender</td>
    <td>Sex of User</td>
  </tr>
  <tr>
    <td>Age</td>
    <td>Age in bins</td>
  </tr>
  <tr>
    <td>Occupation</td>
    <td>Occupation(Masked)</td>
  </tr>
  <tr>
    <td>City_Category</td>
    <td>Category of the City (A,B,C)</td>
  </tr>
  <tr>
    <td>StayInCurrentCityYears</td>
    <td>Number of years of stay in the current city</td>
  </tr>
  <tr>
    <td>Marital_Status</td>
    <td>Marital Status</td>
  </tr>
  <tr>
    <td>ProductCategory1</td>
    <td>Product Category (Masked)</td>
  </tr>
  <tr>
    <td>ProductCategory2</td>
    <td>Product may belong to other category also (Masked)</td>
  </tr>
  <tr>
    <td>ProductCategory3</td>
    <td>Product may belong to other category as well (Masked)</td>
  </tr>
  <tr>
    <td>Purchase</td>
    <td>Purchase Amount (Target Variable)</td>
  </tr>
</table>

<p> The performances of all regression ML models have been evaluated on the basis of predictions of the purchase amount for the test data (test.csv), which contains similar data points as train except for their purchase amount. </p>

<p> Model evaluation has been done using the root mean squared error (RMSE). RMSE is very common and is a suitable general-purpose error metric. Compared to the Mean Absolute Error, RMSE punishes large errors:

Where y hat is the predicted value and y is the original value.</p>

