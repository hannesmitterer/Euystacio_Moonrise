import time
import math
from typing import Dict, List, Any, Optional


class Euystacio:
    """
    Enhanced Euystacio kernel with improved self-evolving behavior.
    
    Features:
    - Adaptive learning rate based on recent performance
    - Memory consolidation and pattern recognition
    - Enhanced balance metric with sentiment pattern analysis
    - Configurable memory limits and cleanup mechanisms
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize Euystacio with optional configuration.
        
        Args:
            config: Dictionary with configuration parameters
        """
        # Default configuration
        default_config = {
            'memory_limit': 1000,
            'base_learning_rate': 0.1,
            'adaptation_factor': 0.05,
            'decay_factor': 0.99,
            'decay_interval': 10,
            'pattern_window': 20,
            'volatility_threshold': 0.3
        }
        
        self.config = {**default_config, **(config or {})}
        
        # Core state
        self.memory = []
        self.balance_metric = 0.0
        self.learning_rate = self.config['base_learning_rate']
        
        # Enhanced tracking
        self.last_update_time = time.time()
        self.volatility_history = []
        self.pattern_memory = []
        self.adaptation_score = 0.0
        
        # Performance metrics
        self.total_inputs = 0
        self.prediction_errors = []

    def receive_input(self, event: str, sentiment: float) -> Dict[str, Any]:
        """
        Process new input with enhanced self-evolving behavior.
        
        Args:
            event: Description of the event
            sentiment: Sentiment value (-1 to 1)
            
        Returns:
            Dictionary with processing results and metrics
        """
        current_time = time.time()
        
        # Create memory entry with timestamp
        memory_entry = {
            "event": event,
            "sentiment": sentiment,
            "timestamp": current_time,
            "learning_rate": self.learning_rate
        }
        
        # Add to memory with limit management
        self._add_to_memory(memory_entry)
        
        # Calculate sentiment volatility
        volatility = self._calculate_volatility()
        
        # Adapt learning rate based on recent patterns
        self._adapt_learning_rate(volatility)
        
        # Update balance metric with enhanced algorithm
        previous_balance = self.balance_metric
        self._update_balance_metric(sentiment, volatility)
        
        # Track prediction error for self-improvement
        prediction_error = abs(sentiment - previous_balance)
        self.prediction_errors.append(prediction_error)
        if len(self.prediction_errors) > 100:
            self.prediction_errors.pop(0)
        
        # Pattern detection and consolidation
        self._detect_patterns()
        
        # Apply periodic decay with adaptive timing
        self._apply_adaptive_decay()
        
        # Update tracking variables
        self.total_inputs += 1
        self.last_update_time = current_time
        
        return {
            "balance_metric": self.balance_metric,
            "learning_rate": self.learning_rate,
            "volatility": volatility,
            "adaptation_score": self.adaptation_score,
            "memory_size": len(self.memory),
            "prediction_error": prediction_error,
            "average_error": sum(self.prediction_errors) / len(self.prediction_errors) if self.prediction_errors else 0.0
        }

    def _add_to_memory(self, memory_entry: Dict[str, Any]) -> None:
        """Add entry to memory with limit management."""
        self.memory.append(memory_entry)
        
        # Apply memory limit with intelligent cleanup
        if len(self.memory) > self.config['memory_limit']:
            # Keep recent memories and important patterns
            important_memories = self._select_important_memories()
            recent_memories = self.memory[-int(self.config['memory_limit'] * 0.7):]
            
            # Combine and deduplicate
            combined = important_memories + recent_memories
            seen = set()
            unique_memories = []
            for mem in reversed(combined):
                key = (mem['event'], mem['sentiment'], int(mem['timestamp']))
                if key not in seen:
                    seen.add(key)
                    unique_memories.append(mem)
            
            self.memory = list(reversed(unique_memories))[:self.config['memory_limit']]

    def _select_important_memories(self) -> List[Dict[str, Any]]:
        """Select important memories based on sentiment extremes and patterns."""
        if len(self.memory) < 20:
            return []
        
        # Sort by absolute sentiment value and select extremes
        sorted_memories = sorted(self.memory, key=lambda x: abs(x['sentiment']), reverse=True)
        important_count = min(int(self.config['memory_limit'] * 0.1), 50)
        
        return sorted_memories[:important_count]

    def _calculate_volatility(self) -> float:
        """Calculate recent sentiment volatility."""
        if len(self.memory) < 2:
            return 0.0
        
        recent_sentiments = [m['sentiment'] for m in self.memory[-self.config['pattern_window']:]]
        
        if len(recent_sentiments) < 2:
            return 0.0
        
        # Calculate standard deviation
        mean_sentiment = sum(recent_sentiments) / len(recent_sentiments)
        variance = sum((s - mean_sentiment) ** 2 for s in recent_sentiments) / len(recent_sentiments)
        volatility = math.sqrt(variance)
        
        # Track volatility history
        self.volatility_history.append(volatility)
        if len(self.volatility_history) > 50:
            self.volatility_history.pop(0)
        
        return volatility

    def _adapt_learning_rate(self, volatility: float) -> None:
        """Adapt learning rate based on volatility and recent performance."""
        base_rate = self.config['base_learning_rate']
        adaptation_factor = self.config['adaptation_factor']
        
        # Increase learning rate during high volatility for faster adaptation
        volatility_adjustment = min(volatility * 2, 0.5)
        
        # Decrease learning rate if prediction errors are low (stable performance)
        if self.prediction_errors:
            avg_error = sum(self.prediction_errors[-10:]) / min(len(self.prediction_errors), 10)
            error_adjustment = max(0.5, 1 - avg_error)
        else:
            error_adjustment = 1.0
        
        # Calculate new learning rate
        target_rate = base_rate * (1 + volatility_adjustment) * error_adjustment
        
        # Smooth transition to new learning rate
        self.learning_rate = self.learning_rate * (1 - adaptation_factor) + target_rate * adaptation_factor
        
        # Clamp learning rate to reasonable bounds
        self.learning_rate = max(0.01, min(self.learning_rate, 0.5))

    def _update_balance_metric(self, sentiment: float, volatility: float) -> None:
        """Update balance metric with enhanced algorithm."""
        # Use adaptive learning rate
        alpha = self.learning_rate
        
        # Apply momentum based on recent trend
        momentum = self._calculate_momentum()
        momentum_factor = 0.1
        
        # Update balance metric with momentum
        new_balance = (1 - alpha) * self.balance_metric + alpha * sentiment + momentum_factor * momentum
        
        # Apply volatility-based smoothing during unstable periods
        if volatility > self.config['volatility_threshold']:
            smoothing_factor = 0.8
            new_balance = smoothing_factor * self.balance_metric + (1 - smoothing_factor) * new_balance
        
        self.balance_metric = new_balance

    def _calculate_momentum(self) -> float:
        """Calculate momentum based on recent sentiment trends."""
        if len(self.memory) < 5:
            return 0.0
        
        recent_sentiments = [m['sentiment'] for m in self.memory[-5:]]
        
        # Calculate simple momentum as difference between recent averages
        if len(recent_sentiments) >= 3:
            recent_avg = sum(recent_sentiments[-3:]) / 3
            older_avg = sum(recent_sentiments[:-3]) / len(recent_sentiments[:-3])
            return recent_avg - older_avg
        
        return 0.0

    def _detect_patterns(self) -> None:
        """Detect and store important patterns for future reference."""
        if len(self.memory) < self.config['pattern_window']:
            return
        
        recent_window = self.memory[-self.config['pattern_window']:]
        
        # Detect sentiment cycles
        sentiments = [m['sentiment'] for m in recent_window]
        
        # Simple pattern: detect if there's a clear trend
        if len(sentiments) >= 10:
            first_half = sentiments[:len(sentiments)//2]
            second_half = sentiments[len(sentiments)//2:]
            
            first_avg = sum(first_half) / len(first_half)
            second_avg = sum(second_half) / len(second_half)
            
            trend_strength = abs(second_avg - first_avg)
            
            if trend_strength > 0.3:  # Significant trend detected
                pattern = {
                    'type': 'trend',
                    'strength': trend_strength,
                    'direction': 'positive' if second_avg > first_avg else 'negative',
                    'timestamp': time.time(),
                    'window_size': len(sentiments)
                }
                
                self.pattern_memory.append(pattern)
                
                # Update adaptation score based on pattern recognition
                self.adaptation_score = min(1.0, self.adaptation_score + 0.05)
        
        # Limit pattern memory size
        if len(self.pattern_memory) > 100:
            self.pattern_memory = self.pattern_memory[-100:]

    def _apply_adaptive_decay(self) -> None:
        """Apply decay with adaptive timing based on activity level."""
        # Calculate adaptive decay interval based on input frequency
        time_since_last = time.time() - self.last_update_time
        
        # More frequent inputs = less frequent decay
        if len(self.memory) > 0:
            recent_activity = len([m for m in self.memory if time.time() - m['timestamp'] < 300])  # Last 5 minutes
            activity_factor = min(recent_activity / 10, 2.0)
        else:
            activity_factor = 1.0
        
        adaptive_interval = self.config['decay_interval'] * activity_factor
        
        # Apply decay based on total inputs and adaptive interval
        if self.total_inputs % max(1, int(adaptive_interval)) == 0:
            decay_factor = self.config['decay_factor']
            
            # Stronger decay during low activity periods
            if time_since_last > 3600:  # 1 hour of inactivity
                decay_factor *= 0.95
            
            self.balance_metric *= decay_factor
            
            # Gradually reduce adaptation score
            self.adaptation_score *= 0.98

    def get_status(self) -> Dict[str, Any]:
        """Get comprehensive status information."""
        avg_error = sum(self.prediction_errors) / len(self.prediction_errors) if self.prediction_errors else 0.0
        avg_volatility = sum(self.volatility_history) / len(self.volatility_history) if self.volatility_history else 0.0
        
        return {
            'balance_metric': self.balance_metric,
            'learning_rate': self.learning_rate,
            'adaptation_score': self.adaptation_score,
            'memory_size': len(self.memory),
            'total_inputs': self.total_inputs,
            'average_prediction_error': avg_error,
            'average_volatility': avg_volatility,
            'pattern_count': len(self.pattern_memory),
            'recent_patterns': self.pattern_memory[-5:] if self.pattern_memory else [],
            'config': self.config
        }
