# --- Build stage: compile the WAR ---
FROM maven:3.9.7-eclipse-temurin-17 AS build
WORKDIR /app
COPY pom.xml .
RUN mvn -q -DskipTests dependency:go-offline
COPY . .
RUN mvn -q -DskipTests package

# --- Runtime stage: Tomcat 11 (Jakarta Servlet 6) ---
FROM tomcat:11.0-jdk17-temurin

# Deploy as ROOT for cleaner URL (/) ; change to EmailListApp.war if you want context path
COPY --from=build /app/target/EmailListApp-1.0-SNAPSHOT.war /usr/local/tomcat/webapps/ROOT.war

ENV CATALINA_OPTS="-Xms256m -Xmx512m"
EXPOSE 8080
CMD ["catalina.sh","run"]




