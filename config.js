/**
 * Euystacio Frontend Configuration
 * 
 * This file contains configuration settings for the Euystacio frontend.
 * Modify these values to customize the behavior and backend connection.
 */

window.EuystacioConfig = {
  // Backend Configuration
  backend: {
    // Primary backend URL - update this with your deployed backend URL
    url: "https://euystacio-backend.onrender.com",
    
    // Fallback URLs to try if primary fails
    fallbackUrls: [
      "http://localhost:5000"
    ],
    
    // Request timeout in milliseconds
    timeout: 10000,
    
    // Retry configuration
    maxRetries: 3,
    retryDelay: 1000
  },
  
  // Authentication Configuration
  auth: {
    // Default user credentials (for demo purposes)
    defaultUser: {
      username: "hannesmitterer",
      password: "moon-rise"
    },
    
    // Session timeout in milliseconds (15 minutes)
    sessionTimeout: 15 * 60 * 1000
  },
  
  // UI Configuration
  ui: {
    // Auto-refresh interval for pulse chart (milliseconds)
    refreshInterval: 15000,
    
    // Chart configuration
    chart: {
      maxDataPoints: 50,
      animationDuration: 1000,
      colors: {
        primary: "#0ff",
        background: "rgba(0,255,255,0.2)"
      }
    },
    
    // Error display configuration
    errorDisplay: {
      duration: 5000, // How long to show error messages
      maxErrors: 5    // Maximum errors to show at once
    }
  },
  
  // Feature Flags
  features: {
    // Enable automatic backend discovery
    autoDiscovery: true,
    
    // Enable enhanced error reporting
    enhancedErrorReporting: true,
    
    // Enable performance metrics display
    showMetrics: true,
    
    // Enable debug mode (shows console logs)
    debugMode: false
  },
  
  // API Endpoints (relative to backend URL)
  endpoints: {
    pulse: "/pulse",
    log: "/log",
    status: "/status",
    metrics: "/metrics",
    kernel: "/kernel",
    info: "/"
  }
};

/**
 * Environment-specific configuration overrides
 * These will override the default configuration based on the hostname
 */
window.EuystacioConfig.environmentOverrides = {
  // Local development
  "localhost": {
    backend: {
      url: "http://localhost:5000"
    },
    features: {
      debugMode: true
    }
  },
  
  // GitHub Pages deployment
  "github.io": {
    features: {
      autoDiscovery: true,
      enhancedErrorReporting: true
    }
  },
  
  // Custom domain deployment
  "your-domain.com": {
    backend: {
      url: "https://your-backend.your-domain.com"
    }
  }
};

/**
 * Apply environment-specific overrides
 */
(function applyEnvironmentConfig() {
  const hostname = window.location.hostname;
  
  for (const [pattern, overrides] of Object.entries(window.EuystacioConfig.environmentOverrides)) {
    if (hostname.includes(pattern)) {
      // Deep merge overrides
      function deepMerge(target, source) {
        for (const key in source) {
          if (source[key] && typeof source[key] === 'object' && !Array.isArray(source[key])) {
            target[key] = target[key] || {};
            deepMerge(target[key], source[key]);
          } else {
            target[key] = source[key];
          }
        }
      }
      
      deepMerge(window.EuystacioConfig, overrides);
      
      if (window.EuystacioConfig.features.debugMode) {
        console.log(`Applied configuration overrides for ${pattern}:`, overrides);
      }
      break;
    }
  }
})();