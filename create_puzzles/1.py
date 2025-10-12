import json
import random
import math
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

class ProfessionalPuzzleGenerator:
    """Professional puzzle generator with dynamic patterns like OTP"""
    
    PATTERN_TYPES = {
        'easy': ['cross', 'square', 'l_shape', 'plus'],
        'medium': ['diamond', 'spiral', 't_shape', 'zigzag'],
        'hard': ['maze', 'web', 'complex_cross', 'interlock'],
        'expert': ['star', 'quantum', 'fractal', 'neural']
    }
    
    @staticmethod
    def generate_dynamic_puzzle(difficulty, rows, cols, num_equations):
        """Generate completely random puzzle pattern like OTP"""
        # Select random pattern based on difficulty
        pattern_type = random.choice(ProfessionalPuzzleGenerator.PATTERN_TYPES[difficulty])
        
        # Generate unique seed for this generation (like OTP)
        seed = f"{difficulty}_{rows}_{cols}_{num_equations}_{random.randint(1000, 9999)}"
        random.seed(seed)
        
        if difficulty == 'easy':
            return ProfessionalPuzzleGenerator._generate_easy_puzzle(rows, cols, num_equations, pattern_type)
        elif difficulty == 'medium':
            return ProfessionalPuzzleGenerator._generate_medium_puzzle(rows, cols, num_equations, pattern_type)
        elif difficulty == 'hard':
            return ProfessionalPuzzleGenerator._generate_hard_puzzle(rows, cols, num_equations, pattern_type)
        else:  # expert
            return ProfessionalPuzzleGenerator._generate_expert_puzzle(rows, cols, num_equations, pattern_type)
    
    @staticmethod
    def _generate_easy_puzzle(rows, cols, num_equations, pattern_type):
        """Easy: Simple equations, clear patterns"""
        grid = [['_' for _ in range(cols)] for _ in range(rows)]
        solution = {}
        equations = []
        
        # Generate simple equations
        for i in range(num_equations):
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            op = random.choice(['+', '-'])
            result = a + b if op == '+' else a - b
            
            if result > 0:  # Ensure positive
                equations.append({'numbers': [a, b, result], 'operation': op})
        
        # Apply pattern
        if pattern_type == 'cross':
            ProfessionalPuzzleGenerator._apply_cross_pattern(grid, equations, solution, 'easy')
        elif pattern_type == 'square':
            ProfessionalPuzzleGenerator._apply_square_pattern(grid, equations, solution, 'easy')
        elif pattern_type == 'l_shape':
            ProfessionalPuzzleGenerator._apply_l_shape_pattern(grid, equations, solution, 'easy')
        else:  # plus
            ProfessionalPuzzleGenerator._apply_plus_pattern(grid, equations, solution, 'easy')
        
        choices = ProfessionalPuzzleGenerator._generate_choices(equations, 12, 1, 20)
        return {'grid': grid, 'solution': solution, 'choices': choices, 'pattern_type': pattern_type}
    
    @staticmethod
    def _generate_medium_puzzle(rows, cols, num_equations, pattern_type):
        """Medium: Includes multiplication, more complexity"""
        grid = [['_' for _ in range(cols)] for _ in range(rows)]
        solution = {}
        equations = []
        
        for i in range(num_equations):
            eq_type = random.choice(['add_sub', 'multiply'])
            
            if eq_type == 'add_sub':
                a = random.randint(5, 20)
                b = random.randint(1, 15)
                op = random.choice(['+', '-'])
                result = a + b if op == '+' else a - b
            else:
                a = random.randint(2, 8)
                b = random.randint(2, 8)
                op = '×'
                result = a * b
            
            if result > 0:
                equations.append({'numbers': [a, b, result], 'operation': op})
        
        if pattern_type == 'diamond':
            ProfessionalPuzzleGenerator._apply_diamond_pattern(grid, equations, solution, 'medium')
        elif pattern_type == 'spiral':
            ProfessionalPuzzleGenerator._apply_spiral_pattern(grid, equations, solution, 'medium')
        elif pattern_type == 't_shape':
            ProfessionalPuzzleGenerator._apply_t_shape_pattern(grid, equations, solution, 'medium')
        else:  # zigzag
            ProfessionalPuzzleGenerator._apply_zigzag_pattern(grid, equations, solution, 'medium')
        
        choices = ProfessionalPuzzleGenerator._generate_choices(equations, 15, 1, 30)
        return {'grid': grid, 'solution': solution, 'choices': choices, 'pattern_type': pattern_type}
    
    @staticmethod
    def _generate_hard_puzzle(rows, cols, num_equations, pattern_type):
        """Hard: Multiple operations, complex patterns"""
        grid = [['_' for _ in range(cols)] for _ in range(rows)]
        solution = {}
        equations = []
        
        for i in range(num_equations):
            # Two-operation equations
            a = random.randint(5, 25)
            b = random.randint(2, 12)
            c = random.randint(2, 12)
            
            op_combo = random.choice([('+', '×'), ('×', '-'), ('-', '+')])
            op1, op2 = op_combo
            
            if op1 == '+' and op2 == '×':
                result = a + b * c
            elif op1 == '×' and op2 == '-':
                result = a * b - c
            else:
                result = a - b + c
            
            if result > 0:
                equations.append({'numbers': [a, b, c, result], 'operations': [op1, op2]})
        
        if pattern_type == 'maze':
            ProfessionalPuzzleGenerator._apply_maze_pattern(grid, equations, solution, 'hard')
        elif pattern_type == 'web':
            ProfessionalPuzzleGenerator._apply_web_pattern(grid, equations, solution, 'hard')
        elif pattern_type == 'complex_cross':
            ProfessionalPuzzleGenerator._apply_complex_cross_pattern(grid, equations, solution, 'hard')
        else:  # interlock
            ProfessionalPuzzleGenerator._apply_interlock_pattern(grid, equations, solution, 'hard')
        
        choices = ProfessionalPuzzleGenerator._generate_choices(equations, 18, 5, 50)
        return {'grid': grid, 'solution': solution, 'choices': choices, 'pattern_type': pattern_type}
    
    @staticmethod
    def _generate_expert_puzzle(rows, cols, num_equations, pattern_type):
        """Expert: Advanced mathematics, extremely complex patterns"""
        grid = [['_' for _ in range(cols)] for _ in range(rows)]
        solution = {}
        equations = []
        
        for i in range(num_equations):
            # Expert level equations
            eq_type = random.choice(['multi_op_div', 'large_numbers', 'complex_frac'])
            
            if eq_type == 'multi_op_div':
                a = random.randint(10, 30)
                b = random.randint(2, 6)
                c = random.randint(5, 20)
                d = random.randint(2, 5)
                
                # Ensure divisible
                while a % b != 0:
                    a = random.randint(10, 30)
                
                result = (a // b) + (c * d)
                equations.append({'numbers': [a, b, c, d, result], 'operations': ['÷', '+', '×']})
            
            elif eq_type == 'large_numbers':
                a = random.randint(20, 50)
                b = random.randint(5, 15)
                c = random.randint(5, 15)
                result = a - b * c
                if result > 0:
                    equations.append({'numbers': [a, b, c, result], 'operations': ['-', '×']})
            
            else:  # complex_frac
                a = random.randint(15, 40)
                b = random.randint(3, 8)
                c = random.randint(10, 25)
                result = (a * b) - c
                if result > 0:
                    equations.append({'numbers': [a, b, c, result], 'operations': ['×', '-']})
        
        if pattern_type == 'star':
            ProfessionalPuzzleGenerator._apply_star_pattern(grid, equations, solution, 'expert')
        elif pattern_type == 'quantum':
            ProfessionalPuzzleGenerator._apply_quantum_pattern(grid, equations, solution, 'expert')
        elif pattern_type == 'fractal':
            ProfessionalPuzzleGenerator._apply_fractal_pattern(grid, equations, solution, 'expert')
        else:  # neural
            ProfessionalPuzzleGenerator._apply_neural_pattern(grid, equations, solution, 'expert')
        
        choices = ProfessionalPuzzleGenerator._generate_choices(equations, 24, 10, 100)
        return {'grid': grid, 'solution': solution, 'choices': choices, 'pattern_type': pattern_type}
    
    # Pattern application methods (simplified for brevity)
    @staticmethod
    def _apply_cross_pattern(grid, equations, solution, difficulty):
        """Apply cross pattern to grid"""
        center_row = len(grid) // 2
        center_col = len(grid[0]) // 2
        
        # Place horizontal equation
        if equations:
            eq = equations[0]
            for i in range(5):
                col = center_col - 2 + i
                if i == 0:
                    grid[center_row][col] = str(eq['numbers'][0])
                elif i == 1:
                    grid[center_row][col] = eq['operation']
                elif i == 2:
                    grid[center_row][col] = str(eq['numbers'][1])
                elif i == 3:
                    grid[center_row][col] = '='
                elif i == 4:
                    grid[center_row][col] = str(eq['numbers'][2])
        
        # Place vertical equation  
        if len(equations) > 1:
            eq = equations[1]
            for i in range(5):
                row = center_row - 2 + i
                if i == 0:
                    grid[row][center_col] = str(eq['numbers'][0])
                elif i == 1:
                    grid[row][center_col] = eq['operation']
                elif i == 2:
                    grid[row][center_col] = str(eq['numbers'][1])
                elif i == 3:
                    grid[row][center_col] = '='
                elif i == 4:
                    grid[row][center_col] = str(eq['numbers'][2])
    
    @staticmethod
    def _apply_diamond_pattern(grid, equations, solution, difficulty):
        """Apply diamond pattern"""
        center_row = len(grid) // 2
        center_col = len(grid[0]) // 2
        
        # Diamond points
        points = [
            (center_row-2, center_col),
            (center_row-1, center_col-1), (center_row-1, center_col+1),
            (center_row, center_col-2), (center_row, center_col+2),
            (center_row+1, center_col-1), (center_row+1, center_col+1),
            (center_row+2, center_col)
        ]
        
        # Place equations at diamond points
        for i, (r, c) in enumerate(points):
            if i < len(equations) and 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                eq = equations[i]
                if len(eq['numbers']) >= 3:
                    grid[r][c] = str(eq['numbers'][0])
    
    # Add other pattern application methods similarly...
    
    @staticmethod
    def _generate_choices(equations, count, min_val, max_val):
        """Generate choice numbers"""
        choices = set()
        
        # Add numbers from equations
        for eq in equations:
            for num in eq['numbers']:
                choices.add(num)
        
        # Add random numbers
        while len(choices) < count:
            choices.add(random.randint(min_val, max_val))
        
        return sorted(list(choices))[:count]

@method_decorator(csrf_exempt, name='dispatch')
class ProfessionalPuzzleView(View):
    """Professional puzzle generation view"""
    
    def get(self, request):
        """Render the main puzzle interface"""
        return render(request, 'puzzle_professional.html')
    
    def post(self, request):
        """Generate professional puzzle"""
        try:
            data = json.loads(request.body)
            difficulty_map = {'1': 'easy', '2': 'medium', '3': 'hard', '4': 'expert'}
            
            difficulty = difficulty_map.get(data.get('difficulty', '1'), 'easy')
            rows = int(data.get('rows', 8))
            cols = int(data.get('cols', 8))
            num_equations = int(data.get('num_equations', 6))
            
            # Generate professional puzzle
            result = ProfessionalPuzzleGenerator.generate_dynamic_puzzle(
                difficulty, rows, cols, num_equations
            )
            
            return JsonResponse({
                'success': True,
                'grid': result['grid'],
                'solution': result['solution'],
                'choices': result['choices'],
                'pattern_type': result['pattern_type'],
                'difficulty': difficulty
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })