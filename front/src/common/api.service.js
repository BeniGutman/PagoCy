import axios from "axios";
import { API_URL } from "./config";


export const ScanService = {
  async getAll() {
    const response = await axios.get(`${API_URL}/scans`);
    return response.data?.scans;
  }
};

export const ResourceService = {
  async getAllForScanId(scanId) {
    const response = await axios.get(`${API_URL}/resources?scan_id=${scanId}`);
    return response.data?.resources;
  }
};
