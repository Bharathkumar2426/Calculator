# Execution Guide — E-Commerce Testing (Selenium + Java)

This guide provides step-by-step instructions to compile and execute the automated testing suite for this project.

---

## 1. Project Overview

This project demonstrates **Black-Box Software Testing** techniques:
- **Equivalence Partitioning (EP)**: Splitting inputs into valid and invalid equivalence classes.
- **Boundary Value Analysis (BVA)**: Evaluating behavior at the minimum, maximum, and boundary edge values.

### Modules Tested
1. **Login Module** (7 test cases: `L01`–`L07`): Format verification, required fields, and password length boundaries (7, 8, 16, 17 characters).
2. **Product Quantity Module** (10 test cases: `Q01`–`Q10`): Integer constraint boundaries for range `[1, 10]`, negative values, decimals, and non-numeric input.
3. **Product Search Module** (6 test cases: `S01`–`S06`): Character length boundaries `[1, 50]`, empty search, and zero-result queries.
4. **Payment Validation Module** (8 test cases: `P01`–`P08`): 16-digit card constraint, MM/YY format & month range `01–12`, 3-digit CVV, and cardholder name presence.

### Key Files
- [pom.xml](file:///c:/Users/dellh/Downloads/EcommerceTestingSelenium/pom.xml): Maven configuration with Selenium Java `4.27.0` and `exec-maven-plugin`.
- [EcommerceTestCases.java](file:///c:/Users/dellh/Downloads/EcommerceTestingSelenium/src/main/java/com/testing/EcommerceTestCases.java): Main test runner and Selenium automation scripts.
- [ecommerce.html](file:///c:/Users/dellh/Downloads/EcommerceTestingSelenium/src/main/resources/ecommerce.html): Offline demo e-commerce web application with client-side validation.

---

## 2. Prerequisites

| Requirement | Minimum Version | Status on this System |
| :--- | :--- | :--- |
| **Java JDK** | JDK 17+ | Installed (`OpenJDK 21`) |
| **Google Chrome** | Latest stable | Installed |
| **IDE Java Tools** | Language Support for Java / Debugger | Installed |
| **Apache Maven** | Maven 3.8+ | Optional (required only for CLI `mvn`) |

> **Note:** Selenium 4 includes **Selenium Manager**, which automatically downloads and matches the correct `ChromeDriver` version for your installed Google Chrome browser. No manual driver download is necessary.

---

## 3. Execution Methods

### Method 1: Run Directly in the IDE (Fastest & Recommended)

Since the Java Extension Pack is installed in your IDE:

1. Open [EcommerceTestCases.java](file:///c:/Users/dellh/Downloads/EcommerceTestingSelenium/src/main/java/com/testing/EcommerceTestCases.java).
2. Locate the `main` method on line 88:
   ```java
   public static void main(String[] args)
   ```
3. Click the **Run** button that appears right above the `main` method signature, or press:
   - **`Ctrl + F5`** (Run without debugging)
   - **`F5`** (Run with debugging)
4. Chrome will launch automatically in a maximized window, run the test suites, close upon completion, and output the summary in the Debug Console / Terminal.

---

### Method 2: Run via Terminal Using Maven Wrapper (Recommended for Terminal)

A self-contained Maven Wrapper (`mvnw.cmd`) has been added to your project root. You do **not** need to install Maven globally or configure PATH.

Open PowerShell in the project directory and run:

```powershell
.\mvnw.cmd clean compile
.\mvnw.cmd exec:java "-Dexec.mainClass=com.testing.EcommerceTestCases"
```

---

### Method 3: Run via System Maven (`mvn`)

If you have global Maven installed and configured on your system PATH:

```powershell
mvn clean compile
mvn exec:java "-Dexec.mainClass=com.testing.EcommerceTestCases"
```

---

### Method 4: Run via Maven GUI in the IDE

1. Open the **Maven** view in the sidebar / Explorer panel.
2. Expand **EcommerceTestingSelenium** > **Plugins** > **exec**.
3. Right-click or click the Play icon next to **`exec:java`**.

---

## 4. Expected Output

During execution, 31 test scenarios run sequentially. The test runner will log the results to standard output:

```text
=== LOGIN: EP and BVA ===
PASS: L01 valid login
PASS: L02 invalid email
PASS: L03 empty email
PASS: L04 password length 7
PASS: L05 password length 8
PASS: L06 password length 16 accepted by format
PASS: L07 password length 17

=== PRODUCT QUANTITY: EP and BVA ===
PASS: Q01 normal valid quantity 5
PASS: Q02 below minimum 0
PASS: Q03 minimum boundary 1
PASS: Q04 just above minimum 2
PASS: Q05 just below maximum 9
PASS: Q06 maximum boundary 10
PASS: Q07 above maximum 11
PASS: Q08 negative quantity
PASS: Q09 decimal quantity
PASS: Q10 non-numeric quantity

=== SEARCH: EP and BVA ===
PASS: S01 valid search
PASS: S02 empty search
PASS: S03 minimum length 1
PASS: S04 maximum length 50
PASS: S05 above maximum length 51
PASS: S06 valid search with no matches

=== PAYMENT: EP and BVA ===
PASS: P01 card length 15
PASS: P02 valid-format details
PASS: P03 card length 17
PASS: P04 card has non-digit
PASS: P05 CVV length 2
PASS: P06 CVV length 4
PASS: P07 empty cardholder name
PASS: P08 invalid expiry month

=== SUMMARY ===
Passed: 31
Failed: 0
Total: 31
```

---

## 5. Troubleshooting & FAQs

- **`mvn : The term 'mvn' is not recognized`**:
  - Run the project using **Method 1** (IDE Run button) which does not require Maven on the CLI PATH, or install Maven using `winget install Apache.Maven`.
- **Chrome fails to launch or version mismatch**:
  - Ensure Google Chrome is updated to the latest version via `Settings > About Chrome`. Selenium Manager will fetch the matching driver automatically.
- **HTML File Not Found**:
  - The script relies on relative path `src/main/resources/ecommerce.html`. Make sure you run commands from the project root directory (`EcommerceTestingSelenium`).
