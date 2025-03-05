import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] A = new int[N];
        for (int i = 0; i < N; i++)
            A[i] = sc.nextInt();
        int[] B = new int[M];
        for (int i = 0; i < M; i++)
            B[i] = sc.nextInt();
        // Please write your code here.
        int ans = 0;
        for (int i =0;i<N;i++){
            int[] arr = new int[N+1];
        
            int c = 0;
            for(int j=i;j<i+M;j++){
                if (j>=N){
                    break;
                }
                c++;
                arr[A[j]] = 1;        
            }
            if (c != M)
                continue;
            int count= 0;
            for(int j=0;j<M;j++){
                    if(arr[B[j]]==1){
                        count++;
                    }
            }
            //System.out.println(count);
            if(count >= M){
                ans ++;
            }
        }
        System.out.println(ans);


    }
}