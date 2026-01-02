let authContext = null;

export const setAuthContext = (context) => {
  authContext = context;
};

export const getAuthContext = () => authContext;
