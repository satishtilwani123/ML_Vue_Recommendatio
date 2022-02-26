<template>
    <!-- Product Card -->
    <div class="card" style="">
        <img class="card-img-top" :src="image" alt="Card image cap">
        <div class="card-body">
            <h5 class="card-title"><router-link :to="{ name:'Recommendation', params:{id: ids, name: title} }">{{ title }}</router-link><strong class="rating">{{ rating }}</strong></h5>
            <a href="#" class="btn btn-primary">Read more</a>
        </div>
    </div>
</template>

<script>

export default {
    name: 'Products',
    props: ['image', 'title', 'rating', 'ids', 'genre'],
}
</script>

<style scoped>
.rating
{
    float: right;
}
.card-title
{
    font-size: 0.8em;
    font-family: Arial, Helvetica, sans-serif;
}
.genre
{
    font-size: 0.8em;
    font-family: Arial, Helvetica, sans-serif;
}
.card img
{
    width: 100%;
    height: 200px;
}
.card
{
    height: 320px;
    margin-top: 7%;
}
.card-body .btn
{
    bottom: 0px;
    left: 0px;
    position: absolute;
    margin: 5%;
}
</style>