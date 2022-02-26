<template>
    <!-- Header -->
    <Header />

    <!-- Movie Description -->
    <div class="container description">
        <div class="row" v-for="product in filteringproduct" :key="product.id">
                <div class="cards" v-if="product.id == $route.params.id">
                    <div class="card-bodys">
                        <div class="row">
                            <img class="col-sm-3 card-imgs img-fluid" :src="product.poster" >
                            <div class="col-sm-8 offset-sm-1">
                                <h5 class="card-name">{{ product.name }}</h5>
                                <h5 class="card-rating">{{ product.rating }}</h5>
                                <p>In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonstrate the visual form of a document or a typeface without relying on meaningful content. Lorem ipsum may be used as a placeholder before the final copy is available. It is also used to temporarily replace text in a process called greeking, which allows designers to consider the form of a webpage.</p>
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                            </div>
                        </div>
                    </div>
                </div>
        </div>

        <!-- Recommended Movies -->
        <div class="row headrecommend">
            <div class="line"></div><h4 class="recommendation">Recommended Movies</h4>
        </div>
        <Productlist :allproducts="APIResult" />
    </div>
</template>

<script>
import { getAPI } from "@/axios";
import Header from '../components/Header.vue'
import Productlist from '../components/Productlist.vue'
export default {
    name: 'Recommendation',
    components: {
        Header,
        Productlist
    },
    data(){
        return{
            filteringproduct: Array,
            APIResult: Array,
        }
    },
    created(){
        this.filteringproduct = [
            {'id': 1, 'name': 'Dead Presidents (1995)', 'rating': 6.8, 'poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMzE0NTI0MTM5MV5BMl5BanBnXkFtZTcwMzYwMTYyMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg', 'genre': 'Action|Crime|Drama'},
            {'id': 608, 'name': 'The AristoCats (1970)', 'rating': 7.1, 'poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4OTg4MDQ4NF5BMl5BanBnXkFtZTgwNjY0MzcxMTE@._V1_UX182_CR0,0,182,268_AL_.jpg', 'genre': 'Animation|Adventure|Comedy'},
            {'id': 244, 'name': 'Immortal Beloved (1994)', 'rating': 7.5, 'poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BNzE3NjQ4MTQyNV5BMl5BanBnXkFtZTYwOTU1MDg4._V1_UX182_CR0,0,182,268_AL_.jpg', 'genre': 'Biography|Drama|Music'},
            {'id': 5294, 'name': 'The Bourne Identity (2002)', 'rating': 7.9, 'poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BM2JkNGU0ZGMtZjVjNS00NjgyLWEyOWYtZmRmZGQyN2IxZjA2XkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_UX182_CR0,0,182,268_AL_.jpg', 'genre': 'Action|Mystery|Thriller'},
            {'id': 54286, 'name': 'Seishun zankoku monogatari (1960)', 'rating': 7.1, 'poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTI3OTEzNjI3N15BMl5BanBnXkFtZTcwMDE5NTYxMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg', 'genre': 'Drama'},
            {'id': 439810, 'name': 'La sierra (2005)', 'rating': 7.7, 'poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTI4NTA3MjY1OF5BMl5BanBnXkFtZTcwMzM2NjA0MQ@@._V1_UY268_CR9,0,182,268_AL_.jpg', 'genre': 'Documentary'}
        ]
    },
    mounted(){
            getAPI
                .get("/recommend", {
                    params: {
                        MovieName: this.$route.params.name,
                    }
                })
                .then(response => {
                    console.log("Recieved data successfully");
                    this.APIResult = response.data
                    console.log(response.data);
                })
                .catch(err => {
                    console.log(err);
                })
    }
}
</script>

<style scoped>
.headrecommend
{
    margin: 10px;
}
.description
{
    margin-top: 10%;
}
.cards
{
    margin: 5%;
}
.card-imgs
{
    border-radius: 2px 2px;
    padding: 30px;
    padding-top: 0px;
}
.rating
{
    float: right;
}
.card-title
{
    font-size: 1em;
    font-family: Arial, Helvetica, sans-serif;
}
.genre
{
    font-size: 0.8em;
    font-family: Arial, Helvetica, sans-serif;
}
.card
{
    height: 350px;
    margin-top: 7%;
}
.card-body .btn
{
    bottom: 0px;
    left: 0px;
    position: absolute;
    margin: 5%;
}
.recommendation
{
    margin-left: 0%;
    margin-bottom: 0%;
    color: white;
    text-shadow: 2px 2px black;
}
.line
{
    width: 1%;
    height: 30px;
    background-color: red;
    display: inline-block;
    margin-right: 5px;
}
.card-name
{
    color: white;
}
.card-rating
{
    color: white;
}
p
{
    color: white
};
</style>