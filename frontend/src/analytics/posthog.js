import posthog from "posthog-js";

const key = import.meta.env.VITE_POSTHOG_KEY;
const host = import.meta.env.VITE_POSTHOG_HOST;

// HARD GUARD — prevents broken builds
if (typeof window !== "undefined" && key && host) {
  posthog.init(key, {
    api_host: host,
    autocapture: false,
    capture_pageview: false,
  });
}

export default posthog;
