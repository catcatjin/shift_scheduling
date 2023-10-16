<template>
    <div>
      <h1>護士班表</h1>
      <table class="table table-bordered table-responsive">
        <thead class="thead-dark">
          <tr>
            <th scope="col">護士</th>
            <th v-for="day in days" :key="day" scope="col">天 {{ day }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(nurse, index) in nurses" :key="index">
            <td>{{ nurse.name }}</td>
            <td 
            v-for="day in days" 
            :key="day" 
            :class="shiftColor(nurse.shifts[day])"
            >
            {{ nurse.shifts[day] || '' }}
          </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    created() {
    this.assignFirstDayShifts();
    },
    data() {
      return {
        nurses: Array.from({ length: 12 }, (_, i) => `護士 ${i + 1}`),
        days: Array.from({ length: 28 }, (_, i) => i + 1),
        shifts: ['OF', 'D', 'N', 'E'],
        colors: {
        OF: 'bg-white',
        D: 'bg-success',
        N: 'bg-warning',
        E: 'bg-primary',
        },
        firstDayShifts: ['D', 'D', 'D', 'D', 'D', 'E', 'E', 'E', 'E', 'N', 'N', 'N'],
      };
    },
    methods: {
    shiftColor(shift) {
    return this.colors[shift] || 'bg-white';
     },
    assignFirstDayShifts() {
    this.nurses = this.nurses.map((nurse, index) => ({
        name: nurse,
        shifts: {
        1: this.firstDayShifts[index] || 'OF',
        },
    }));
    },
    
    },
  };
  </script>