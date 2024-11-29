FROM node:20-alpine AS builder
ARG VITE_API_CLIENT_BASE_URL
ENV VITE_API_CLIENT_BASE_URL=${VITE_API_CLIENT_BASE_URL}
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:stable-alpine AS production
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=builder /app/dist ./
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 4173
CMD ["nginx", "-g", "daemon off;"]
