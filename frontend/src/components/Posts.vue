<template>
    <h1>Публикации пользователя {{currentUser.name}}</h1> 

    <div class="" v-for = "post in filteredPosts" :key="post.id">
        <hr/>
        <h2>{{post.title}}</h2>
        <p>{{post.content}}</p>
        <hr/>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "get-posts",
    data() {
        return {
            users: null,
            posts: null,
            id: this.$route.path.slice(-1) 
        };
    },
    created() {
        axios.get("http://127.0.0.1:5000/post").then(response => this.posts = response.data)
        axios.get("http://127.0.0.1:5000/users").then(response => this.users = response.data)
    },
    computed: {
        filteredPosts(){
            return this.posts.filter(post => post.owner == this.id)
        },
        currentUser(){
            return this.users.filter(user => user.id == this.id)[0]
        }
    }
}
 
</script>