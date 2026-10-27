package com.testing;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions;

import java.nio.file.Paths;
import java.time.Duration;

/**
 * Demonstrates Equivalence Partitioning (EP) and Boundary Value Analysis (BVA)
 * against the local demo application bundled in src/main/resources.
 *
 * Demo login credentials: user@gmail.com / Pass1234
 * This is an educational demo, not a real e-commerce/payment system.
 */
public class EcommerceTestCases {
    private static WebDriver driver;
    private static WebDriverWait wait;
    private static int passed = 0;
    private static int failed = 0;

    // Adjustable delay settings to clearly observe browser actions
    private static final int ACTION_DELAY_MS = 400; // Delay between typing/clicking
    private static final int RESULT_DELAY_MS = 800; // Pause after result is shown

    private static void pause(long millis) {
        try {
            Thread.sleep(millis);
        } catch (InterruptedException ignored) {
            Thread.currentThread().interrupt();
        }
    }

    private static void scrollTo(WebElement element) {
        try {
            ((JavascriptExecutor) driver).executeScript(
                    "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element);
        } catch (Exception ignored) {
        }
    }
    //start of the program

    private static void openApp() {
        String page = Paths.get("src/main/resources/ecommerce.html")
                           .toAbsolutePath().toUri().toString();
        driver.get(page);
    }

    private static String text(String id) {
        return wait.until(ExpectedConditions.visibilityOfElementLocated(By.id(id)))
                   .getText();
    }

    private static void check(String testName, boolean condition) {
        if (condition) {
            passed++;
            System.out.println("PASS: " + testName);
        } else {
            failed++;
            System.out.println("FAIL: " + testName);
        }
    }

    private static void loginTest(String email, String password,
                                  String expectedMessage, String name) {
        openApp();
        WebElement emailField = driver.findElement(By.id("email"));
        scrollTo(emailField);
        pause(ACTION_DELAY_MS);
        emailField.sendKeys(email);
        pause(ACTION_DELAY_MS);
        driver.findElement(By.id("password")).sendKeys(password);
        pause(ACTION_DELAY_MS);
        driver.findElement(By.id("loginBtn")).click();
        check(name, text("loginMessage").equals(expectedMessage));
        pause(RESULT_DELAY_MS);
    }

    private static void quantityTest(String quantity,
                                     boolean expectedValid, String name) {
        openApp();
        WebElement field = driver.findElement(By.id("quantity"));
        scrollTo(field);
        pause(ACTION_DELAY_MS);
        field.sendKeys(quantity);
        pause(ACTION_DELAY_MS);
        driver.findElement(By.id("addToCart")).click();
        String result = text("quantityMessage");
        check(name, expectedValid
                ? result.equals("Quantity accepted.")
                : result.equals("Quantity must be an integer from 1 to 10."));
        pause(RESULT_DELAY_MS);
    }

    private static void searchTest(String search,
                                   String expectedMessage, String name) {
        openApp();
        WebElement field = driver.findElement(By.id("search"));
        scrollTo(field);
        pause(ACTION_DELAY_MS);
        field.sendKeys(search);
        pause(ACTION_DELAY_MS);
        driver.findElement(By.id("searchBtn")).click();
        check(name, text("searchMessage").equals(expectedMessage));
        pause(RESULT_DELAY_MS);
    }

    private static void paymentTest(String card, String expiry, String cvv,
                                    String holder, String expectedMessage,
                                    String name) {
        openApp();
        WebElement cardField = driver.findElement(By.id("cardNumber"));
        scrollTo(cardField);
        pause(ACTION_DELAY_MS);
        cardField.sendKeys(card);
        pause(ACTION_DELAY_MS);
        driver.findElement(By.id("expiry")).sendKeys(expiry);
        pause(ACTION_DELAY_MS);
        driver.findElement(By.id("cvv")).sendKeys(cvv);
        pause(ACTION_DELAY_MS);
        driver.findElement(By.id("cardholder")).sendKeys(holder);
        pause(ACTION_DELAY_MS);
        driver.findElement(By.id("payBtn")).click();
        check(name, text("paymentMessage").equals(expectedMessage));
        pause(RESULT_DELAY_MS);
    }

    public static void main(String[] args) {
        driver = new ChromeDriver();
        driver.manage().window().maximize();
        wait = new WebDriverWait(driver, Duration.ofSeconds(5));

        try {
            System.out.println("=== LOGIN: EP and BVA ===");
            loginTest("user@gmail.com", "Pass1234",
                    "Login successful.", "L01 valid login");
            loginTest("invalid-email", "Pass1234",
                    "Invalid email format.", "L02 invalid email");
            loginTest("", "Pass1234",
                    "Email and password are required.", "L03 empty email");
            loginTest("user@gmail.com", "Pass123",
                    "Password must contain 8–16 characters.", "L04 password length 7");
            loginTest("user@gmail.com", "Pass1234",
                    "Login successful.", "L05 password length 8");
            loginTest("user@gmail.com", "Pass123456789012",
                    "Incorrect email or password.", "L06 password length 16 accepted by format");
            loginTest("user@gmail.com", "Pass1234567890123",
                    "Password must contain 8–16 characters.", "L07 password length 17");

            System.out.println("\n=== PRODUCT QUANTITY: EP and BVA ===");
            quantityTest("5", true, "Q01 normal valid quantity 5");
            quantityTest("0", false, "Q02 below minimum 0");
            quantityTest("1", true, "Q03 minimum boundary 1");
            quantityTest("2", true, "Q04 just above minimum 2");
            quantityTest("9", true, "Q05 just below maximum 9");
            quantityTest("10", true, "Q06 maximum boundary 10");
            quantityTest("11", false, "Q07 above maximum 11");
            quantityTest("-1", false, "Q08 negative quantity");
            quantityTest("2.5", false, "Q09 decimal quantity");
            quantityTest("abc", false, "Q10 non-numeric quantity");

            System.out.println("\n=== SEARCH: EP and BVA ===");
            searchTest("Laptop", "Search completed for: Laptop", "S01 valid search");
            searchTest("", "Please enter a search term.", "S02 empty search");
            searchTest("A", "Search completed for: A", "S03 minimum length 1");
            searchTest("A".repeat(50), "Search completed for: " + "A".repeat(50),
                    "S04 maximum length 50");
            searchTest("A".repeat(51), "Search must not exceed 50 characters.",
                    "S05 above maximum length 51");
            searchTest("XYZ123Unknown", "No products found.", "S06 valid search with no matches");

            System.out.println("\n=== PAYMENT: EP and BVA ===");
            paymentTest("123456789012345", "12/29", "123", "Test User",
                    "Card number must contain exactly 16 digits.", "P01 card length 15");
            paymentTest("1234567890123456", "12/29", "123", "Test User",
                    "Payment details accepted for demo validation.", "P02 valid-format details");
            paymentTest("12345678901234567", "12/29", "123", "Test User",
                    "Card number must contain exactly 16 digits.", "P03 card length 17");
            paymentTest("123456789012345a", "12/29", "123", "Test User",
                    "Card number must contain exactly 16 digits.", "P04 card has non-digit");
            paymentTest("1234567890123456", "12/29", "12", "Test User",
                    "CVV must contain exactly 3 digits.", "P05 CVV length 2");
            paymentTest("1234567890123456", "12/29", "1234", "Test User",
                    "CVV must contain exactly 3 digits.", "P06 CVV length 4");
            paymentTest("1234567890123456", "12/29", "123", "",
                    "Cardholder name is required.", "P07 empty cardholder name");
            paymentTest("1234567890123456", "13/29", "123", "Test User",
                    "Expiry month must be 01–12.", "P08 invalid expiry month");

        } finally {
            pause(2500);
            driver.quit();
            System.out.println("\n=== SUMMARY ===");
            System.out.println("Passed: " + passed);
            System.out.println("Failed: " + failed);
            System.out.println("Total: " + (passed + failed));
        }
    }
}
