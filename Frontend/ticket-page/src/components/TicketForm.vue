<template>
  <div class="ticket-form">
    <h2>Create a New Ticket</h2>
    <form @submit.prevent="createTicket">
      <div class="mb-3">
        <label for="title" class="form-label">Title:</label>
        <input type="text" id="title" v-model="ticket.title" class="form-control" required />
      </div>

      <div class="mb-3">
        <label for="description" class="form-label">Description:</label>
        <textarea id="description" v-model="ticket.description" class="form-control" required></textarea>
      </div>

      <div class="mb-3">
        <label for="user_info" class="form-label">Contact Information:</label>
        <input type="text" id="user_info" v-model="ticket.user_info" class="form-control" required />
      </div>

      <div class="mb-3"  hidden>
        <label for="status" class="form-label">Status:</label>
        <input type="text" id="status" v-model="ticket.status" class="form-control" value="Pending" />
      
      </div>

      <button type="submit" class="btn btn-success">Create Ticket</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      ticket: {
        title: "",
        description: "",
        user_info: "",
        status: "Pending"
      }
    };
  },
  methods: {
    async createTicket() {
      try {
        const response = await axios.post("http://127.0.0.1:5000/tickets", this.ticket);
        console.log("Ticket Created:", response.data);
        this.$emit("ticket-created", response.data);  // Emit event to refresh the ticket list
        this.resetForm();
      } catch (error) {
        console.error("Error creating ticket:", error);
      }
    },
    resetForm() {
      this.ticket = {
        title: "",
        description: "",
        user_info: "",
        status: "Pending"
      };
    }
  }
};
</script>

<style scoped>
.ticket-form {
  max-width: 500px;
  margin: auto;
}

form {
  display: flex;
  flex-direction: column;
}

button {
  margin-top: 10px;
}
</style>
