 Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        scan.close();
        
        // Split the string using the regular expression to match non-alphabetic characters
        String[] tokens = s.split("[^A-Za-z]+");
        
        // Filter out any empty tokens resulting from leading, trailing, or multiple spaces
        List<String> validTokens = new ArrayList<>();
        for (String token : tokens) {
            if (!token.isEmpty()) {
                validTokens.add(token);
            }
        }

        // Print the number of valid tokens
        System.out.println(validTokens.size());
        
        // Print each token on a new line
        for (String token : validTokens) {
            System.out.println(token);
        }
    }