<template>
  <div>
    <!-- Ticket Card View -->
    <div
      class="ticket-card"
      :class="statusClass"
      v-if="!editMode"
      @click="editMode = true"
    >
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">{{ ticket.title }}</h5>
          <p class="card-text"><strong>Description:</strong> {{ ticket.description }}</p>
          <p class="card-text"><strong>Contact Information:</strong> {{ ticket.user_info }}</p>
          <p class="card-text"><strong>Status:</strong> {{ ticket.status }}</p>
          <p class="card-text"><strong>Created Timestamp:</strong> {{ ticket.created_at }}</p>
          <p v-if="ticket.updated_at"><strong>Update Timestamp:</strong> {{ ticket.updated_at }}</p>
        </div>
      </div>
    </div>

    <!-- Ticket Edit Mode -->
    <div class="ticket-edit" v-else>
      <div class="form-group">
        <label for="status-select"><strong>Status:</strong></label>
        <select id="status-select" class="form-control" v-model="editableStatus">
          <option value="Pending">Pending</option>
          <option value="Accepted">Accepted</option>
          <option value="Resolved">Resolved</option>
          <option value="Rejected">Rejected</option>
        </select>
      </div>

      <div class="button-group">
        <button class="btn btn-primary" @click="submitEdit">Submit</button>
        <button class="btn btn-secondary" @click="cancelEdit">Cancel</button>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  props: ["ticket"],
  data() {
    return {
      editMode: false,
      editableStatus: this.ticket.status
    };
  },
  computed: {
    // Computed property to return the class based on the ticket status
    statusClass() {
      switch (this.ticket.status) {
        case 'Pending':
          return 'border-warning'; // Yellowish border for Pending
        case 'Accepted':
          return 'border-primary'; // Blue border for Accepted
        case 'Resolved':
          return 'border-success'; // Green border for Resolved
        case 'Rejected':
          return 'border-danger'; // Red border for Rejected
        default:
          return ''; // Default border color
      }
    }
  },
  methods: {
    async submitEdit() {
      try {
        // Send the update request to the backend
        await axios.put(`http://127.0.0.1:5000/tickets/${this.ticket.id}`, {
          status: this.editableStatus
        });

        // Notify the parent to refresh the ticket list
        this.$emit("ticket-updated");

        this.editMode = false; // Exit edit mode
      } catch (error) {
        console.error("Error updating ticket:", error);
        alert("Failed to update the ticket. Please try again.");
      }
    },
    cancelEdit() {
      this.editableStatus = this.ticket.status;
      this.editMode = false;
    }
  }
};
</script>
<style scoped>
.ticket-card,
.ticket-edit {
  border: 2px solid #ddd;
  padding: 15px;
  border-radius: 8px;
  background-color: #f9f9f9;
}

.ticket-card:hover {
  cursor: pointer;
  background-color: #ececec;
}

.button-group {
  margin-top: 10px;
  
}

button {
  margin-right: 10px;
}

/* Bootstrap border classes will color the border based on status */
.border-warning {
  border-color: #ffc107; /* Yellow for Pending */
}

.border-primary {
  border-color: #007bff; /* Blue for Accepted */
}

.border-success {
  border-color: #28a745; /* Green for Resolved */
}

.border-danger {
  border-color: #dc3545; /* Red for Rejected */
}
</style>
