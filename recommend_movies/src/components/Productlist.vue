<template>
    <!-- Loop Through List of Movies -->
    <div class="container">
        <div class="row">
            <div class="col-md-2" v-for="product in allproducts" :key="product.id">
                <Products :ids="product.id" :image="product.poster" :title="product.name" :rating="product.rating" :genre="product.genre"/>
            </div>
        </div>
    </div>
</template>

<script>
import Products from './Products.vue'

export default {
    name: 'Productlist',
    props: ['allproducts'],
    components: {
        Products,
    },
}
</script>

<style scoped>
.container
{
  margin-top: 5%;
}
</style>