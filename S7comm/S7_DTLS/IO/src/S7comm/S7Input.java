package S7comm;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlTransient;
import se.uu.it.dtlsfuzzer.execute.AbstractInputExecutor;
import se.uu.it.dtlsfuzzer.execute.ExecutionContext;


@XmlAccessorType(XmlAccessType.FIELD)
public abstract class S7Input {

    @XmlTransient
    private AbstractInputExecutor preferredExecutor = null;

    @XmlAttribute(name="extendedWait", required = false)
    private Integer extendedWait;

    protected S7Input(){
    }

    public AbstraInputExecutor getPreferredExcutor() {
        return preferredExecutor;
    }

    public void setPreferredExecutor(AbstractInputExecutor preferredExecutor){
        this.preferredExecutor = preferredExecutor;
    }

    public boolean isEnabled(State state, ExecutionContext context){
        return true;
    }


}
