import re
from termcolor import colored
from pyfiglet import Figlet

class PasswordStrengthAnalyzer:
    def __init__(self):
        self.password = ""
        self.strength = 0
        self.feedback = []
        self.colors = {
            "weak": "red",
            "medium": "yellow",
            "strong": "green",
            "excellent": "blue"
        }
        
    def display_banner(self):
        f = Figlet(font='slant')
        print(colored(f.renderText('Password Analyzer'), 'cyan'))
        print(colored("="*60, 'magenta'))
        print(colored("🔒 Evaluate your password strength with advanced metrics", 'white'))
        print(colored("="*60, 'magenta') + "\n")
        
    def get_password(self):
        from getpass import getpass
        self.password = getpass(colored("🔑 Enter your password: ", 'yellow'))
        return self.password
        
    def analyze_length(self):
        length = len(self.password)
        if length < 8:
            self.feedback.append(colored("❌ Too short (min 8 characters)", 'red'))
            return 0
        elif 8 <= length <= 11:
            self.feedback.append(colored(f"✓ Fair length ({length} chars)", 'yellow'))
            return 1
        elif 12 <= length <= 15:
            self.feedback.append(colored(f"✓ Good length ({length} chars)", 'green'))
            return 2
        else:
            self.feedback.append(colored(f"✓ Excellent length ({length} chars)", 'blue'))
            return 3
            
    def analyze_complexity(self):
        score = 0
        # Check for uppercase letters
        if re.search(r'[A-Z]', self.password):
            score += 1
            self.feedback.append(colored("✓ Contains uppercase letters", 'green'))
        else:
            self.feedback.append(colored("❌ Missing uppercase letters", 'red'))
            
        # Check for lowercase letters
        if re.search(r'[a-z]', self.password):
            score += 1
            self.feedback.append(colored("✓ Contains lowercase letters", 'green'))
        else:
            self.feedback.append(colored("❌ Missing lowercase letters", 'red'))
            
        # Check for numbers
        if re.search(r'[0-9]', self.password):
            score += 1
            self.feedback.append(colored("✓ Contains numbers", 'green'))
        else:
            self.feedback.append(colored("❌ Missing numbers", 'red'))
            
        # Check for special characters
        if re.search(r'[^A-Za-z0-9]', self.password):
            score += 1
            self.feedback.append(colored("✓ Contains special characters", 'green'))
        else:
            self.feedback.append(colored("❌ Missing special characters", 'red'))
            
        return score
        
    def check_common_patterns(self):
        common_patterns = [
            'password', '123456', 'qwerty', 'admin', 'welcome',
            'sunshine', 'iloveyou', 'football', 'monkey', 'abc123'
        ]
        
        if self.password.lower() in common_patterns:
            self.feedback.append(colored("❌ Warning: Common password detected", 'red'))
            return -2
        return 0
        
    def check_entropy(self):
        import math
        charset = 0
        
        if re.search(r'[a-z]', self.password):
            charset += 26
        if re.search(r'[A-Z]', self.password):
            charset += 26
        if re.search(r'[0-9]', self.password):
            charset += 10
        if re.search(r'[^A-Za-z0-9]', self.password):
            charset += 32  # common special chars
            
        if charset == 0:
            return 0
            
        entropy = len(self.password) * math.log2(charset)
        
        if entropy < 28:
            self.feedback.append(colored(f"⚠ Low entropy ({entropy:.1f} bits)", 'red'))
            return 0
        elif 28 <= entropy < 36:
            self.feedback.append(colored(f"✓ Moderate entropy ({entropy:.1f} bits)", 'yellow'))
            return 1
        elif 36 <= entropy < 60:
            self.feedback.append(colored(f"✓ High entropy ({entropy:.1f} bits)", 'green'))
            return 2
        else:
            self.feedback.append(colored(f"✓ Excellent entropy ({entropy:.1f} bits)", 'blue'))
            return 3
            
    def calculate_strength(self):
        self.strength = 0
        self.strength += self.analyze_length()
        self.strength += self.analyze_complexity()
        self.strength += self.check_common_patterns()
        self.strength += self.check_entropy()
        
        # Cap the score between 0 and 10
        self.strength = max(0, min(10, self.strength))
        
    def display_result(self):
        print("\n" + colored("🔍 Analysis Results:", 'cyan', attrs=['bold']))
        print(colored("-"*40, 'magenta'))
        
        for item in self.feedback:
            print(f"  {item}")
            
        print("\n" + colored("🏆 Overall Strength:", 'cyan', attrs=['bold']))
        
        strength_level = ""
        if self.strength <= 3:
            strength_level = "Weak"
            color = self.colors["weak"]
        elif 4 <= self.strength <= 6:
            strength_level = "Medium"
            color = self.colors["medium"]
        elif 7 <= self.strength <= 8:
            strength_level = "Strong"
            color = self.colors["strong"]
        else:
            strength_level = "Excellent"
            color = self.colors["excellent"]
            
        # Visual strength meter
        filled = '█' * self.strength
        empty = '░' * (10 - self.strength)
        print(f"  {colored(filled + empty, color)} {self.strength}/10")
        print(f"  {colored(strength_level, color, attrs=['bold'])}\n")
        
    def run(self):
        self.display_banner()
        while True:
            self.password = self.get_password()
            if not self.password:
                print(colored("⚠ Please enter a password!", 'red'))
                continue
                
            self.feedback = []
            self.calculate_strength()
            self.display_result()
            
            choice = input(colored("🔁 Test another password? (y/n): ", 'yellow')).lower()
            if choice != 'y':
                print(colored("\n🔒 Stay secure! Goodbye!\n", 'cyan'))
                break

if __name__ == "__main__":
    try:
        analyzer = PasswordStrengthAnalyzer()
        analyzer.run()
    except KeyboardInterrupt:
        print(colored("\n🔒 Session terminated. Stay secure!", 'red'))