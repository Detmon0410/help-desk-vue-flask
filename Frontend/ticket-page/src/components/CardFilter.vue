<template>
    <div class="card-filter mb-4">
      <div class="row">
        <!-- Filter by Status -->
        <div class="col-md-6">
          <label for="status-filter">Filter by Status</label>
          <select
            id="status-filter"
            class="form-control"
            v-model="selectedStatus"
            @change="updateFilter"
          >
            <option value="">All</option>
            <option value="Pending">Pending</option>
            <option value="Accepted">Accepted</option>
            <option value="Resolved">Resolved</option>
            <option value="Rejected">Rejected</option>
          </select>
        </div>
  
        <!-- Sort by Field -->
        <div class="col-md-6">
          <label for="sort-field">Sort by</label>
          <select
            id="sort-field"
            class="form-control"
            v-model="selectedSortField"
            @change="updateSort"
          >
            <option value="created_at">Date Created (New)</option>
            <option value="created_at_old">Date Created (Old)</option>
            <option value="updated_at">Date Updated (New)</option>            
            <option value="updated_at_old">Date Updated (Old)</option>
            <option value="status">Status</option>
           
          </select>
        </div>
      </div>
    </div>
  </template>
  
  
  <script>
  export default {
    data() {
      return {
        selectedStatus: "", // Selected status for filtering
        selectedSortField: "created_at", // Selected field for sorting
      };
    },
    methods: {
      updateFilter() {
        // Emit the selected status to the parent component
        this.$emit("filter-updated", this.selectedStatus);
      },
      updateSort() {
        // Emit the selected sort field to the parent component
        this.$emit("sort-updated", this.selectedSortField);
      },
    },
  };
  </script>
  
  <style scoped>
  .card-filter {
    background-color: #f8f9fa;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin-top: 20px;
  }
  </style>
  