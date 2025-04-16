import java.util.concurrent.*;
import java.util.regex.*;
import java.util.*;
import java.io.*;
import java.nio.file.*;
import java.nio.charset.StandardCharsets;


public class KeywordCounter {

    // Sekwencyjna metoda zliczania wystąpień słowa
    public static int countKeywordSequential(String text, String keyword) {
        if (text == null || keyword == null || keyword.isEmpty()) {
            return 0;
        }

        String regex = "(?i)" + Pattern.quote(keyword); // (?i) - ignorowanie wielkości liter
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(text);

        int count = 0;
        while (matcher.find()) {
            count++;
        }

        return count;
    }

    // Wielowątkowa metoda zliczania wystąpień słowa
    public static int countKeywordMultithreaded(String text, String keyword, int numThreads) throws InterruptedException, ExecutionException {
        if (text == null || keyword == null || keyword.isEmpty()) {
            return 0;
        }

        String regex = "(?i)" + Pattern.quote(keyword); // (?i) - ignorowanie wielkości liter
        Pattern pattern = Pattern.compile(regex);

        // Podziel tekst na fragmenty
        int fragmentSize = text.length() / numThreads;
        ExecutorService executor = Executors.newFixedThreadPool(numThreads);
        List<Future<Integer>> results = new ArrayList<>();

        for (int i = 0; i < numThreads; i++) {
            final int start = i * fragmentSize;
            final int end = (i == numThreads - 1) ? text.length() : (i + 1) * fragmentSize;
            final String fragment = text.substring(start, end);

            // Zlecanie zadań w wątkach
            Future<Integer> result = executor.submit(() -> {
                Matcher matcher = pattern.matcher(fragment);
                int count = 0;
                while (matcher.find()) {
                    count++;
                }
                return count;
            });
            results.add(result);
        }

        // Zbieranie wyników z wątków
        int totalCount = 0;
        for (Future<Integer> result : results) {
            totalCount += result.get();
        }

        executor.shutdown();
        return totalCount;
    }

    public static void main(String[] args) throws InterruptedException, ExecutionException {
        String filePath = "data/Lorem_Ipsum_1GB.txt";  // Ścieżka do pliku

        // Zmienna przechowująca tekst z pliku
        StringBuilder text = new StringBuilder();

        // Czytanie pliku linia po linii
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath, StandardCharsets.UTF_8))) {
            String line;

            while ((line = reader.readLine()) != null) {
                text.append(line).append("\n");
            }
        } catch (IOException e) {
            e.printStackTrace();  // W przypadku błędu odczytu
        }

        // Definicja słowa kluczowego oraz liczby wątków
        String keyword = "sit";
        int numThreads = 4;

        // Sekwencyjne zliczanie
        long startTime = System.nanoTime();
        int resultSequential = countKeywordSequential(text.toString(), keyword);
        long endTime = System.nanoTime();
        System.out.println("Liczba wystąpień słowa '" + keyword + "' (metoda sekwencyjna): " + resultSequential);
        System.out.println("Czas wykonania sekwencyjnego: " + (endTime - startTime) + " nanosekund");

        // Wielowątkowe zliczanie
        startTime = System.nanoTime();
        int resultMultithreaded = countKeywordMultithreaded(text.toString(), keyword, numThreads);
        endTime = System.nanoTime();
        System.out.println("Liczba wystąpień słowa '" + keyword + "' (metoda wielowątkowa): " + resultMultithreaded);
        System.out.println("Czas wykonania wielowątkowego: " + (endTime - startTime) + " nanosekund");
    }
}
