import java.util.Random;
import java.util.Scanner;

public class Rps {
    private static final String[] MOVES = {"rock", "paper", "scissors"};
    private static final Random random = new Random();

    private static String computerMove() {
        return MOVES[random.nextInt(MOVES.length)];
    }

    private static String outcome(String player, String computer) {
        if (player.equals(computer)) return "TIE";
        if ((player.equals("rock") && computer.equals("scissors"))
                || (player.equals("scissors") && computer.equals("paper"))
                || (player.equals("paper") && computer.equals("rock"))) {
            return "PLAYER_WIN";
        }
        return "COMPUTER_WIN";
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int playerWins = 0, computerWins = 0, ties = 0;

        while (true) {
            System.out.print("Enter move (rock/paper/scissors) or quit: ");
            if (!scanner.hasNextLine()) break;
            String input = scanner.nextLine().trim().toLowerCase();

            if (input.equals("quit") || input.equals("q")) break;

            boolean valid = false;
            for (String m : MOVES) {
                if (m.equals(input)) { valid = true; break; }
            }
            if (!valid) {
                System.out.println("Invalid input. Please enter rock, paper, scissors, or quit.");
                continue;
            }

            String computer = computerMove();
            String result = outcome(input, computer);
            System.out.println("Computer chose: " + computer);

            if (result.equals("PLAYER_WIN")) {
                playerWins++;
                System.out.println("You win this round!");
            } else if (result.equals("COMPUTER_WIN")) {
                computerWins++;
                System.out.println("Computer wins this round!");
            } else {
                ties++;
                System.out.println("It's a tie!");
            }
            System.out.println("Score — You: " + playerWins + " | Computer: " + computerWins + " | Ties: " + ties);
        }

        System.out.println("\nFinal Score — You: " + playerWins + " | Computer: " + computerWins + " | Ties: " + ties);
        scanner.close();
    }
}
