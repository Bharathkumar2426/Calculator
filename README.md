# E-Commerce Testing using Java + Selenium (EP and BVA)

## Requirements
- JDK 17 or newer
- Maven 3.8+ (or a current Maven version)
- Google Chrome
- Internet connection for Maven to download Selenium dependencies the first time

## Run in VS Code (Windows PowerShell)
1. Extract the ZIP file.
2. Open the extracted `EcommerceTestingSelenium` folder in VS Code.
3. Open Terminal > New Terminal.
4. Check installations:
   ```powershell
   java -version
   mvn -version
   ```
5. Run:
   ```powershell
   mvn clean compile
   mvn exec:java "-Dexec.mainClass=com.testing.EcommerceTestCases"
   ```

Selenium Manager normally detects/manages ChromeDriver automatically. Keep Chrome installed and updated.

## Included files
- `pom.xml`: Maven project and Selenium dependency
- `src/main/java/com/testing/EcommerceTestCases.java`: Selenium automation
- `src/main/resources/ecommerce.html`: local demo e-commerce page

## How it works
The Java program opens the bundled HTML file directly in Chrome. No separate web server or real Amazon account is needed. It tests login, quantity, search, and payment field validation using EP and BVA and prints PASS/FAIL assertions.

Demo login:
- Email: `user@gmail.com`
- Password: `Pass1234`

## Sample validation assumptions
- Password: 8–16 characters
- Quantity: integer 1–10
- Search: 1–50 characters
- Card number: exactly 16 digits
- Expiry: MM/YY format and month 01–12
- CVV: exactly 3 digits
- Cardholder name: required

This is an educational validation demo only. It does not connect to a payment gateway, charge cards, or validate real card details. Do not enter real payment data.

## Notes
- If Maven is not recognized, install Maven and add its `bin` folder to PATH, then restart VS Code.
- If `mvn clean compile` fails, confirm JDK is installed and `JAVA_HOME`/PATH are configured.
- The Java program's PASS/FAIL checks compare the displayed message with the expected message.
