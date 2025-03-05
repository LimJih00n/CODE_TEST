import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextInt();
        }
        int[] B = new int[M];
        for (int i = 0; i < M; i++) {
            B[i] = sc.nextInt();
        }

        Map<Integer, Integer> bFreq = new HashMap<>();
        for (int num : B) {
            bFreq.put(num, bFreq.getOrDefault(num, 0) + 1);
        }

        int ans = 0;
        Map<Integer, Integer> windowFreq = new HashMap<>();
        for (int i = 0; i < M; i++) {
            windowFreq.put(A[i], windowFreq.getOrDefault(A[i], 0) + 1);
        }

        if (windowFreq.equals(bFreq)) {
            ans++;
        }

        for (int i = M; i < N; i++) {
            int oldVal = A[i - M];
            windowFreq.put(oldVal, windowFreq.get(oldVal) - 1);
            if (windowFreq.get(oldVal) == 0) {
                windowFreq.remove(oldVal);
            }

            int newVal = A[i];
            windowFreq.put(newVal, windowFreq.getOrDefault(newVal, 0) + 1);

            if (windowFreq.equals(bFreq)) {
                ans++;
            }
        }

        System.out.println(ans);
    }
}
