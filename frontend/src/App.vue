<template>
  <div class="container">
    <h1>User Management</h1>

    <form @submit.prevent="saveUser">
      <input v-model="form.name" placeholder="Name" required />
      <input v-model="form.email" placeholder="Email" required />
      <input v-model="form.password" placeholder="Password" required />

      <button type="submit">
        {{ form.id ? "Update" : "Create" }}
      </button>
    </form>

    <hr />

    <ul>
      <li v-for="user in users" :key="user.id">
        {{ user.name }} - {{ user.email }}

        <button @click="editUser(user)">Edit</button>
        <button @click="deleteUser(user.id)">Delete</button>
      </li>
    </ul>
  </div>
</template>

<script>
import api from "./services/api";

export default {
  data() {
    return {
      users: [],
      form: {
        id: null,
        name: "",
        email: "",
        password: "",
      },
    };
  },

  mounted() {
    this.loadUsers();
  },

  methods: {
    async loadUsers() {
      const { data } = await api.get("/users");
      this.users = data;
    },

    async saveUser() {
      if (this.form.id) {
        await api.put(`/users/${this.form.id}/`, this.form);
      } else {
        await api.post("/users/", this.form);
      }

      this.resetForm();
      this.loadUsers();
    },

    editUser(user) {
      this.form = { ...user, password: "" };
    },

    async deleteUser(id) {
      await api.delete(`/users/${id}`);
      this.loadUsers();
    },

    resetForm() {
      this.form = {
        id: null,
        name: "",
        email: "",
        password: "",
      };
    },
  },
};
</script>

<style>
.container {
  max-width: 600px;
  margin: auto;
  font-family: Arial;
}
input {
  margin: 5px;
}
button {
  margin-left: 5px;
}
</style>
