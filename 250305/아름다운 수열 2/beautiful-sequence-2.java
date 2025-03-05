import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static final int MAX_N = 100;
    
    public static int n, m;
    public static int[] arr1 = new int[MAX_N];
    public static int[] arr2 = new int[MAX_N];
    public static int[] tmp = new int[MAX_N];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 입력
        n = sc.nextInt();
        m = sc.nextInt();
        for(int i = 0; i < n; i++)
            arr1[i] = sc.nextInt();
        for(int i = 0; i < m; i++)
            arr2[i] = sc.nextInt();
        
        Arrays.sort(arr2, 0, m);
        
        // 모든 구간의 시작점을 잡아봅니다.
        int cnt = 0;
        for(int i = 0; i <= n - m; i++) {
            for(int j = 0; j < m; j++)
                tmp[j] = arr1[i + j];
            Arrays.sort(tmp, 0, m);
            
            boolean issame = true;
            for(int j = 0; j < m; j++)
                if(tmp[j] != arr2[j]) {
                    issame = false;
                    break;
                }
            
            if(issame)
                cnt++;
        }
                            
        System.out.print(cnt);
    }
}
