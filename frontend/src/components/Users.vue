<template>
    <table>
        <tr>
            <th>City</th>
            <th>Name</th>
            <th>id</th>
        </tr>
        <tr v-for="user in users" :key="user.id">
            <td>{{user.id}}</td>
            <td><router-link :to="{ name: 'user_id', params: { id: user.id }}">{{user.name}}</router-link></td>
            <td>{{user.city}}</td>
        </tr>
    </table>

</template>

<script>
import axios from "axios";

export default {
    name: "get-users",
    data() {
        return {
            users: null
        };
    },
    created() {
        axios.get("http://127.0.0.1:5000/users").then(response => this.users = response.data)
    }
}
 
</script>

<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>