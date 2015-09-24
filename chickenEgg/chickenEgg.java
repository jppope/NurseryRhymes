/**
* @method ChickenVsEgg
* @author Ray Carrender
*/

public class ChickenVsEgg {
    public static String whoCameFirst(String answer) throws OutOfMemoryError {
        return whoCameFirst((answer.equals("chicken") ?  "egg" : "chicken"));
    }
    public static void main(String[] args) {
        String result = "";
        try {
            result = whoCameFirst(result);
        } catch (OutOfMemoryError oom) {
            System.out.print(result + " came first");
        }
    }
}