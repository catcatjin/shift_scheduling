import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://localhost:5000",
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

export default {
  async getNurseSchedule() {
    const response = await apiClient.get("/api/nurse-schedule");
    return response.data;
  },
};