package array.sort;

public class QuickSort {
    public static void main(String[] args) {

        int[] arr = {3,9,4,7,5,0,1,6,8,2};
        printArray(arr);
        quickSort(arr);
        printArray(arr);
    }

    private static void printArray(int[] arr) {
        for(int data : arr) {
            System.out.print(data + ", ");
        }
        System.out.println();
    }

    private static void quickSort(int[] arr) {
        quickSort(arr, 0, arr.length - 1);
    }

    private static void quickSort(int[] arr, int start, int end) {
        int part = partition(arr, start, end);
        if(start < part - 1) { // 왼쪽방이 1개 이하가 아니면
            quickSort(arr, start, part - 1);
        }
        if(part < end) { // 오른쪽방이 1개 이하가 아니면
            quickSort(arr, part, end);
        }
    }

    private static int partition(int[] arr, int start, int end) {

        int pivot = arr[(start + end) / 2];
        while(start <= end) {
            while(arr[start] < pivot) start++;
            while(arr[end] > pivot) end--;
            if(start <= end) {
                swap(arr, start, end);
                start++;
                end--;
            }
        }
        return start;
    }

    private static void swap(int[] arr, int start, int end) {
        int tmp = arr[start];
        arr[start] = arr[end];
        arr[end] = tmp;
    }

}