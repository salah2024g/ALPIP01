import { APP_CONFIG } from "@/config";


test(
  "application config",
  () => {

    expect(
      APP_CONFIG.name
    ).toBe("ALPIP");

  }
);
