from pydub import AudioSegment
import numpy as np
import simpleaudio as sa 
import os


def convert_to_8bit_simple(input_file, output_file="8-bit-song-simple", sample_rate=8000, bit_depth=8):
    """
    Simple 8-bit conversion with basic sample rate and bit depth reduction.
    This is the original algorithm.
    """
    # Load audio file
    audio = AudioSegment.from_file(input_file)

    # Reducir tasa de muestreo
    audio = audio.set_frame_rate(sample_rate)
    audio = audio.set_sample_width(bit_depth // 8)

    # Aplicar distorsion
    samples = np.array(audio.get_array_of_samples())
    samples = np.clip(samples, -2**(bit_depth-1), 2**(bit_depth-1)-1)

    # Crear nuevo segmento de audio
    new_audio = AudioSegment(
        samples.tobytes(),
        frame_rate=sample_rate,
        sample_width=bit_depth // 8,
        channels=audio.channels
    )

    # Guardar archivo
    if output_file:
        if not output_file.endswith('.wav'):
            output_file += '.wav'
        new_audio.export(output_file, format="wav")
        print(f"Simple 8-bit version saved as: {output_file}")
    
    return new_audio


def convert_to_8bit(input_file, output_file="8-bit-song", sample_rate=8000, bit_depth=8, 
                   square_wave_effect=0.3, quantize_factor=0.8, distortion=0.2):
    """
    Convert audio to 8-bit style with various retro effects.
    
    Parameters:
    - input_file: Path to input audio file
    - output_file: Path to output audio file (without extension)
    - sample_rate: Target sample rate (lower = more retro)
    - bit_depth: Target bit depth (8 is classic 8-bit)
    - square_wave_effect: Amount of square wave transformation (0-1)
    - quantize_factor: Strength of quantization effect (0-1)
    - distortion: Amount of distortion to add (0-1)
    """
    # Load audio file
    audio = AudioSegment.from_file(input_file)
    
    # Reduce sample rate (more dramatic for 8-bit feel)
    audio = audio.set_frame_rate(sample_rate)
    
    # Get samples as numpy array
    samples = np.array(audio.get_array_of_samples())
    
    # Apply bit depth reduction (bit crushing)
    max_val = 2**(bit_depth-1) - 1
    
    # Quantization effect (reduces effective resolution)
    if quantize_factor > 0:
        quantize_steps = int(max(2, (2**bit_depth) * (1 - quantize_factor)))
        samples = (samples // quantize_steps) * quantize_steps
    
    # Square wave transformation (makes waveforms more digital/square)
    if square_wave_effect > 0:
        samples_normalized = samples / max_val
        square_samples = np.sign(samples_normalized) * np.power(np.abs(samples_normalized), 0.3) * max_val
        samples = samples * (1 - square_wave_effect) + square_samples * square_wave_effect
    
    # Add some distortion
    if distortion > 0:
        samples = samples * (1 + distortion * np.random.uniform(-0.1, 0.1, size=len(samples)))
    
    # Hard clip to ensure we stay within bit depth range
    samples = np.clip(samples, -max_val, max_val).astype(np.int16)
    
    # Create new audio segment
    new_audio = AudioSegment(
        samples.tobytes(),
        frame_rate=sample_rate,
        sample_width=bit_depth // 4,  # Ensure we have at least 16-bit container
        channels=audio.channels
    )
    
    # Add final touch - slight volume boost to compensate for bit reduction
    new_audio = new_audio + 3
    
    # Save file with extension
    if output_file:
        if not output_file.endswith('.wav'):
            output_file += '.wav'
        new_audio.export(output_file, format="wav")
        print(f"Enhanced 8-bit version saved as: {output_file}")
    
    return new_audio


def convert_to_chiptune(input_file, output_file="chiptune-song", sample_rate=11025, 
                       bit_depth=8, arpeggio_effect=0.2):
    """
    Convert audio to chiptune style with classic video game console effects.
    
    Parameters:
    - input_file: Path to input audio file
    - output_file: Path to output audio file (without extension)
    - sample_rate: Target sample rate (11025 is common for chiptunes)
    - bit_depth: Target bit depth
    - arpeggio_effect: Amount of arpeggio-like effect (0-1)
    """
    # Load audio file
    audio = AudioSegment.from_file(input_file)
    
    # Reduce sample rate to chiptune standard
    audio = audio.set_frame_rate(sample_rate)
    
    # Get samples as numpy array
    samples = np.array(audio.get_array_of_samples())
    max_val = 2**(bit_depth-1) - 1
    
    # Apply hard quantization (very characteristic of chiptunes)
    quantize_steps = 16  # Fewer steps = more "steppy" sound
    samples = (samples // quantize_steps) * quantize_steps
    
    # Apply pulse-wave like effect (very square, like NES)
    samples_normalized = samples / np.max(np.abs(samples))
    pulse_samples = np.sign(samples_normalized) * max_val * 0.8
    samples = samples * 0.2 + pulse_samples * 0.8
    
    # Add "arpeggio" effect (rapid note changes common in chiptunes)
    if arpeggio_effect > 0:
        # Create a tremolo-like effect that mimics arpeggios
        tremolo = np.sin(np.linspace(0, 2 * np.pi * 8, len(samples))) * arpeggio_effect
        samples = samples * (1 + tremolo)
    
    # Hard clip to ensure we stay within range
    samples = np.clip(samples, -max_val, max_val).astype(np.int16)
    
    # Create new audio segment
    new_audio = AudioSegment(
        samples.tobytes(),
        frame_rate=sample_rate,
        sample_width=2,  # 16-bit container
        channels=audio.channels
    )
    
    # Save file with extension
    if output_file:
        if not output_file.endswith('.wav'):
            output_file += '.wav'
        new_audio.export(output_file, format="wav")
        print(f"Chiptune version saved as: {output_file}")
    
    return new_audio


# Example usage with different parameter combinations
if __name__ == "__main__":
    input_file = "holy-pipes.mp3"
    
    # Check if file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
    else:
        # Original simple algorithm
        convert_to_8bit_simple(
            input_file, 
            "holy_pipes_simple_8bit.wav"
        )
        
        # Enhanced 8-bit version (more extreme effects)
        convert_to_8bit(
            input_file, 
            "holy_pipes_enhanced_8bit.wav",
            sample_rate=6000,
            bit_depth=6,
            square_wave_effect=0.5,
            quantize_factor=0.9,
            distortion=0.3
        )
        
        # More balanced 8-bit version
        convert_to_8bit(
            input_file, 
            "holy_pipes_8bit.wav",
            sample_rate=8000,
            bit_depth=8,
            square_wave_effect=0.3,
            quantize_factor=0.7,
            distortion=0.15
        )
        
        # Chiptune version (NES/GameBoy style)
        convert_to_chiptune(
            input_file, 
            "holy_pipes_chiptune.wav",
            sample_rate=11025,
            arpeggio_effect=0.3
        )