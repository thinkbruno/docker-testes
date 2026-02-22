<template>
  <div v-if="toast.show" :class="['toast', toast.type]">
    {{ toast.message }}
  </div>
  <div class="container">
    <div class="card">
      <h1>Teste - CRUD de Usuários</h1>

      <div class="form">
        <div class="form-row">
          <input v-model="form.name" placeholder="Nome" />
          <input v-model="form.email" placeholder="Email" />
          <input v-model="form.password" type="password" placeholder="Password" />
        </div>

        <div class="form-actions">
          <button class="btn-primary" @click="saveUser" :disabled="loading">
            {{ loading ? "Salvando..." : form.id ? "Editar" : "Salvar" }}
          </button>
        </div>
      </div>
      <div v-if="loading" class="loading">
        Carregando...
      </div>
      <ul v-if="!loading" class="user-list">
        <li v-for="user in users" :key="user.id" class="user-item">
          <div>
            <strong>{{ user.name }}</strong>
            <div style="font-size: 0.9rem; opacity: 0.7">
              {{ user.email }}
            </div>
          </div>

          <div class="user-actions">
            <button @click="editUser(user)">Editar</button>
            <button class="btn-danger" @click="deleteUser(user.id)">
              Apagar
            </button>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import api from "./services/api";

export default {
  data() {
    return {
      users: [],
      loading: false,
      saving: false,
      toast: {
        show: false,
        message: "",
        type: "success", // success | error
      },
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
    showToast(message, type = "success") {
      this.toast = { show: true, message, type };
      setTimeout(() => {
        this.toast.show = false;
      }, 3000);
    },

    async loadUsers() {
      this.loading = true;
      try {
        const response = await api.get("/users/");
        this.users = response.data || [];
      } catch (error) {
        this.showToast("Erro ao carregar usuários", "error");
      } finally {
        this.loading = false;
      }
    },

    async saveUser() {
      this.saving = true;
      try {
        const payload = {
          name: this.form.name,
          email: this.form.email,
          password: this.form.password,
        };

        if (this.form.id) {
          await api.put(`/users/${this.form.id}`, payload);
          this.showToast("Usuário atualizado com sucesso");
        } else {
          await api.post("/users/", payload);
          this.showToast("Usuário criado com sucesso");
        }

        this.resetForm();
        this.loadUsers();
      } catch (error) {
        this.showToast(
          error.response?.data?.error || "Erro ao salvar usuário",
          "error"
        );
      } finally {
        this.saving = false;
      }
    },

    editUser(user) {
      this.form = {
        id: user.id,
        name: user.name,
        email: user.email,
        password: "",
      };
    },

    async deleteUser(id) {
      try {
        await api.delete(`/users/${id}`);
        this.showToast("Usuário removido com sucesso");
        this.loadUsers();
      } catch (error) {
        this.showToast("Erro ao deletar usuário", "error");
      }
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