<template>
  <div class="page-container">
    <!-- Ticket creation form -->
    <TicketForm @ticket-created="fetchTickets" />
    <h2 class="text-center mt-4">Ticket List</h2> <!-- Added label here -->
    <!-- Card Filter for sorting and filtering -->
    <CardFilter 
      @filter-updated="applyFilter" 
      @sort-updated="applySort" 
    />

    <!-- Title for the Ticket List -->
   

    <!-- Ticket list -->
    <div class="container mt-4">
      <div class="row">
        <TicketCard 
          v-for="ticket in paginatedTickets" 
          :key="ticket.id" 
          :ticket="ticket" 
          @ticket-updated="fetchTickets" 
          class="col-md-4 mb-4"
        />
      </div>
    </div>

    <!-- Pagination Controls -->
    <div class="pagination-container text-center mt-4">
      <button 
        class="btn btn-primary" 
        @click="goToPreviousPage" 
        :disabled="currentPage === 1"
      >
        Previous
      </button>
      <span class="mx-3">Page {{ currentPage }} of {{ totalPages }}</span>
      <button 
        class="btn btn-primary" 
        @click="goToNextPage" 
        :disabled="currentPage === totalPages"
      >
        Next
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import TicketForm from "@/components/TicketForm.vue";
import TicketCard from "@/components/TicketCard.vue";
import CardFilter from "@/components/CardFilter.vue";

export default {
  components: {
    TicketForm,
    CardFilter,
    TicketCard,
  },
  data() {
    return {
      tickets: [], // Holds the list of all tickets
      filterStatus: "", // Tracks the selected status filter
      sortField: "created_at", // Tracks the selected sort field
      currentPage: 1, // Tracks the current page
      ticketsPerPage: 9, // Number of tickets to display per page
    };
  },
  computed: {
  filteredTickets() {
    let filtered = [...this.tickets];

    // Apply status filter
    if (this.filterStatus) {
      filtered = filtered.filter(ticket => ticket.status === this.filterStatus);
    }

    // Apply sorting logic
    if (this.sortField === "status") {
      const statusOrder = { Pending: 1, Accepted: 2, Resolved: 3, Rejected: 4 };
      filtered.sort((a, b) => statusOrder[a.status] - statusOrder[b.status]);
    } else {
      // Sort by created_at, showing all tickets, even those with null/undefined updated_at
      if (this.sortField === "created_at") {
        filtered.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));
      } 
      else if (this.sortField === "created_at_old") {
        filtered.sort((a, b) => new Date(a.created_at) - new Date(b.created_at));
      } 
      // Sort by updated_at, excluding tickets with null/undefined updated_at
      else if (this.sortField === "updated_at") {
        filtered = filtered.filter(ticket => ticket.updated_at !== null && ticket.updated_at !== undefined);
        filtered.sort((a, b) => new Date(b.updated_at) - new Date(a.updated_at));
      }
      else if (this.sortField === "updated_at_old") {
        filtered = filtered.filter(ticket => ticket.updated_at !== null && ticket.updated_at !== undefined);
        filtered.sort((a, b) => new Date(a.updated_at) - new Date(b.updated_at)); // Older updates first
      }
    }

    return filtered;
  },
  // Paginate the filtered tickets
  paginatedTickets() {
    const startIndex = (this.currentPage - 1) * this.ticketsPerPage;
    return this.filteredTickets.slice(startIndex, startIndex + this.ticketsPerPage);
  },
  // Calculate total pages based on ticketsPerPage
  totalPages() {
    return Math.ceil(this.filteredTickets.length / this.ticketsPerPage);
  }
},
  mounted() {
    this.fetchTickets(); // Fetch tickets when the component is mounted
  },
  methods: {
    async fetchTickets() {
      try {
        const response = await axios.get("http://127.0.0.1:5000/tickets");
        this.tickets = response.data; // Populate the tickets array with API data
      } catch (error) {
        console.error("Error fetching tickets:", error);
      }
    },
    applyFilter(status) {
      this.filterStatus = status; // Update the filter status based on CardFilter input
    },
    applySort(field) {
      this.sortField = field; // Update the sort field based on CardFilter input
    },
    // Move to the next page
    goToNextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
    // Move to the previous page
    goToPreviousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    }
  },
};
</script>
<style scoped>
.page-container {
  padding-top: 40px; /* Adds space at the top of the page */
  padding-bottom: 40px; /* Adds space at the bottom of the page */
}

.ticket-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.pagination-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

button {
  margin: 0 10px;
}
</style>
