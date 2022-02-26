<template>
  <!-- Header -->
  <Header />

  <!-- Jumbotron -->
  <div class="paralax-mf bg-image">
        <div class="overlay-mf"></div>
  </div>

  <!-- ProductList -->
  <Productlist class="prodlist" :allproducts="filteringproduct" />
</template>

<script>
import Productlist from '../components/Productlist.vue'
import Header from '../components/Header.vue'

export default {
  name: 'Movies',
  components: {
    Productlist,
    Header,
  },
  data(){
    return{
      filteringproduct: Array
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
  }
}
</script>

<style scoped>
.prodlist
{
  margin-top: -80px;
}
.paralax-mf
{
    position: relative;
    padding: 8rem 0;
    background: url(../assets/images/netflix.jpg);
    height: 600px;
}
.bg-image {
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
  background-position: center center;
}
@media (max-width: 1024px) {
  .bg-image {
    background-attachment: scroll;
  }
}
.overlay-mf {
  position: absolute;
  top: 0;
  left: 0px;
  padding: 0;
  height: 100%;
  width: 100%;
  opacity: 0.7;
}
</style>
