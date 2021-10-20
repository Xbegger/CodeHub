package basic.VariableType;

public class Modifier {
    String version = "1.5.1";
    boolean processOrder(){
        return true;
    }

    // private 修饰符
    public class Logger{
        private String format;
        public String getFormat(){
            return this.format;
        }
        public void setFormat(String format){
            this.format = format;
        }
    }
    class Speaker{

    }
    // protected 修饰符
    class AudioPlayer{
        protected boolean openSpeaker(Speaker sp){
            //
            return false;
        }
    }
    class StreamingAudioPlayer extends AudioPlayer{
        @Override
        protected boolean openSpeaker(Speaker sp) {
            return super.openSpeaker(sp);
        }
    }
    public static void main(String[] args) {

    }
}
