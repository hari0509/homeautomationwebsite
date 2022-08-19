const { response } = require('express');
const express = require('express');
const MongoClient = require('mongodb').MongoClient
const hostname = '0.0.0.0'
const app = express()
var database
app.use(express.json())

app.get('/', (req, res) => {
    database.collection('movie').find({}).toArray((err, result) => {
        if (err) throw err
        res.send(result)
        console.log(result)
    })
   
 })
app.listen(5000 ,() => {
    MongoClient.connect('mongodb+srv://harimongo:harimongo3@cluster0.ektwvgh.mongodb.net/?retryWrites=true&w=majority', {useNewUrlParser: true}, (error, result) =>{
        if(error) throw error
        database = result.db("moviesDB")
        console.log("sucess rate")
    })
})