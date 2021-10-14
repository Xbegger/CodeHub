package S7comm;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;


public class State {

    private static final Logger LOGGER = LogManager.getLoger();

    private final ContextContainer contextContainer = new ContextContainer();

    private Config config = null;
}
