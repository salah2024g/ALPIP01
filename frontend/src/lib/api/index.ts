import { APP_CONFIG } from "@/config";


export const apiClient =
  new (require("./client").ApiClient)(
    APP_CONFIG.apiBaseUrl
  );
