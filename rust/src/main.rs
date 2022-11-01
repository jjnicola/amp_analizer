use std::fs::{File};
use ndarray::{Array, Axis};
use core::f32::consts::PI;

fn main() {
    let sample_rate = 44100;
    let t = Array::linspace (0.0, 1.0, sample_rate);

    let mut samples = Array::<f32, _>::zeros(0);
    let mut end = false;
    let amplitude = i16::MAX;

    println!("Generating sample audio...");
    for power in 2..6 {

        if end == true {break};

        for i in 1 .. 11 {
            let freq: f32;

            if i != 1 {
                freq = (10i32.pow(power) as f32) * (i as f32).log10();
            } else {
                freq = 10i32.pow(power - 1) as f32;
            }

            if freq >= 5000.0 {
                end = true;
                break;
            }
            let chunk = t.map(|x|  ((amplitude as f32) * (*x as f32) * 2.0 * PI * freq).sin());
            samples.append(Axis(0), chunk.view()).unwrap();
        }
    }
    let mut file_out = File::create("sample_audio.wav").unwrap();

    let head = wav_io::new_header(sample_rate as u32, 32, true, false);
    wav_io::write_to_file(&mut file_out, &head, &samples.to_vec()).unwrap();

    println!("Finished writing sample_audio.wav");
}
